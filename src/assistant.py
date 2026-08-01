"""Retrieval-based music assistant with simple guardrails and confidence scoring."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from src.recommender import load_songs, recommend_songs


@dataclass
class AssistantResponse:
    """Structured response returned by the assistant."""

    answer: str
    retrieved_songs: List[Dict[str, Any]]
    confidence: float
    guardrail_message: Optional[str] = None
    profile: Optional[Dict[str, Any]] = None


class MusicAssistant:
    """A lightweight retrieval-augmented assistant for music recommendations."""

    def __init__(self, songs_path: Optional[Path | str] = None) -> None:
        default_path = Path(__file__).resolve().parents[1] / "data" / "songs.csv"
        self.songs_path = Path(songs_path or default_path)
        self.logger = logging.getLogger("music_assistant")
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(levelname)s:%(name)s:%(message)s"))
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.INFO)

    def respond_to_request(self, request: str, songs: Optional[Sequence[Dict[str, Any]]] = None, k: int = 5) -> AssistantResponse:
        """Generate a response for a user request using retrieval and lightweight reasoning."""
        if not request or not str(request).strip():
            self.logger.warning("Received empty request")
            return AssistantResponse(
                answer="",
                retrieved_songs=[],
                confidence=0.05,
                guardrail_message="Please share a short description of the mood, activity, or vibe you're looking for so I can suggest songs.",
            )

        request_text = str(request).strip()
        if songs is None:
            songs = load_songs(str(self.songs_path))

        profile = self._infer_profile(request_text)
        retrieved_songs = self._retrieve_songs(request_text, list(songs), k=k)
        if not retrieved_songs:
            retrieved_songs = [song for song, _, _ in recommend_songs(profile, list(songs), k=k)]

        answer = self._build_answer(request_text, profile, retrieved_songs)
        confidence = self._score_confidence(request_text, retrieved_songs, profile)
        self.logger.info("Responded to request with %s songs and confidence %.2f", len(retrieved_songs), confidence)
        return AssistantResponse(answer=answer, retrieved_songs=retrieved_songs, confidence=confidence, profile=profile)

    def _infer_profile(self, request: str) -> Dict[str, Any]:
        text = request.lower()

        favorite_genre = "pop"
        if any(term in text for term in ["lofi", "study", "sleep", "chill", "calm"]):
            favorite_genre = "lofi"
        elif any(term in text for term in ["rock", "intense", "workout", "run", "energetic"]):
            favorite_genre = "rock"
        elif any(term in text for term in ["jazz", "relax", "coffee", "soft"]):
            favorite_genre = "jazz"

        favorite_mood = "happy"
        if any(term in text for term in ["chill", "calm", "study", "sleep", "relax"]):
            favorite_mood = "chill"
        elif any(term in text for term in ["intense", "workout", "run", "energetic"]):
            favorite_mood = "energetic"
        elif any(term in text for term in ["focus", "focused", "concentrate"]):
            favorite_mood = "focused"

        target_energy = 0.8
        if any(term in text for term in ["chill", "calm", "study", "sleep", "relax", "quiet"]):
            target_energy = 0.35
        elif any(term in text for term in ["intense", "workout", "run", "energetic"]):
            target_energy = 0.9
        elif any(term in text for term in ["focus", "focused"]):
            target_energy = 0.5

        likes_acoustic = any(term in text for term in ["acoustic", "calm", "chill", "study", "sleep"])

        return {
            "favorite_genre": favorite_genre,
            "favorite_mood": favorite_mood,
            "target_energy": target_energy,
            "likes_acoustic": likes_acoustic,
        }

    def _retrieve_songs(self, request: str, songs: Sequence[Dict[str, Any]], k: int) -> List[Dict[str, Any]]:
        tokens = self._tokenize(request)
        if not tokens:
            return []

        ranked: List[tuple[int, Dict[str, Any]]] = []
        for song in songs:
            text_blob = " ".join(
                [
                    str(song.get("genre", "")),
                    str(song.get("mood", "")),
                    str(song.get("title", "")),
                    str(song.get("artist", "")),
                ]
            ).lower()
            overlap = sum(1 for token in tokens if token in text_blob)
            if overlap > 0:
                ranked.append((overlap, song))

        ranked.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in ranked[:k]]

    def _build_answer(self, request: str, profile: Dict[str, Any], songs: Sequence[Dict[str, Any]]) -> str:
        profile_summary = (
            f"{profile['favorite_genre']} / {profile['favorite_mood']} / energy {profile['target_energy']:.2f}"
        )
        headline = f"I interpreted your request as a {profile_summary} vibe."
        if not songs:
            return headline + " I could not find a strong match in the current catalog."

        bullet_points = [f"- {song['title']} by {song['artist']} ({song['genre']}, {song['mood']})" for song in songs[:3]]
        return headline + "\n" + "\n".join(bullet_points)

    def _score_confidence(self, request: str, songs: Sequence[Dict[str, Any]], profile: Dict[str, Any]) -> float:
        if not request.strip():
            return 0.05
        overlap_score = min(0.6, 0.2 + 0.1 * len(songs))
        profile_score = 0.2 if profile else 0.0
        confidence = min(0.95, overlap_score + profile_score)
        return round(confidence, 2)

    def _tokenize(self, request: str) -> List[str]:
        lowered = request.lower()
        tokens = re.findall(r"[a-z]+", lowered)
        stop_words = {"for", "the", "a", "an", "i", "want", "need", "give", "me", "my", "and", "or", "to", "of"}
        return [token for token in tokens if token not in stop_words and len(token) > 2]
