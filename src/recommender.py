import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union


@dataclass
class Song:
    """Represents a song and its attributes."""

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's taste preferences."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """OOP implementation of the recommendation logic."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs that best match the user's profile."""
        scored_songs = []
        for song in self.songs:
            score, _ = score_song(_user_profile_to_dict(user), _song_to_dict(song))
            scored_songs.append((score, song))

        scored_songs.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a particular song was recommended."""
        _, reasons = score_song(_user_profile_to_dict(user), _song_to_dict(song))
        return "; ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numeric values to floats."""
    with open(csv_path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        songs = []
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs


def score_song(user_prefs: Dict, song: Union[Dict, Song]) -> Tuple[float, List[str]]:
    """Score a single song against a user profile and explain the result."""
    prefs = _normalize_user_prefs(user_prefs)
    song_data = _song_to_dict(song)
    score = 0.0
    reasons = []

    genre_match = song_data.get("genre", "").lower() == prefs["favorite_genre"].lower()
    if genre_match:
        score += 2.0
        reasons.append("genre match (+2.0)")

    mood_match = song_data.get("mood", "").lower() == prefs["favorite_mood"].lower()
    if mood_match:
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_value = float(song_data.get("energy", 0.5))
    energy_gap = abs(energy_value - prefs["target_energy"])
    energy_similarity = max(0.0, 1.0 - energy_gap)
    energy_points = energy_similarity * 1.5
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    valence_target = 0.7 if prefs["favorite_mood"].lower() in {"happy", "energetic", "focused"} else 0.4
    valence_value = float(song_data.get("valence", 0.5))
    valence_gap = abs(valence_value - valence_target)
    valence_similarity = max(0.0, 1.0 - valence_gap)
    valence_points = valence_similarity * 0.75
    score += valence_points
    reasons.append(f"valence similarity (+{valence_points:.2f})")

    if prefs["likes_acoustic"] and float(song_data.get("acousticness", 0.5)) > 0.7:
        score += 0.5
        reasons.append("acoustic preference (+0.5)")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top-k results with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]


def _normalize_user_prefs(user_prefs: Union[Dict, UserProfile]) -> Dict:
    if isinstance(user_prefs, UserProfile):
        return {
            "favorite_genre": user_prefs.favorite_genre,
            "favorite_mood": user_prefs.favorite_mood,
            "target_energy": user_prefs.target_energy,
            "likes_acoustic": user_prefs.likes_acoustic,
        }

    return {
        "favorite_genre": user_prefs.get("favorite_genre", user_prefs.get("genre", "")),
        "favorite_mood": user_prefs.get("favorite_mood", user_prefs.get("mood", "")),
        "target_energy": float(user_prefs.get("target_energy", user_prefs.get("energy", 0.5))),
        "likes_acoustic": bool(user_prefs.get("likes_acoustic", False)),
    }


def _song_to_dict(song: Union[Dict, Song]) -> Dict:
    if isinstance(song, Song):
        return {
            "id": song.id,
            "title": song.title,
            "artist": song.artist,
            "genre": song.genre,
            "mood": song.mood,
            "energy": song.energy,
            "tempo_bpm": song.tempo_bpm,
            "valence": song.valence,
            "danceability": song.danceability,
            "acousticness": song.acousticness,
        }
    return song


def _user_profile_to_dict(user: UserProfile) -> Dict:
    return _normalize_user_prefs(user)
