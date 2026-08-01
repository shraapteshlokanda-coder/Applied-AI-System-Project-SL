from src.recommender import Song, UserProfile, Recommender
from src.assistant import MusicAssistant

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_assistant_handles_empty_query_gracefully():
    assistant = MusicAssistant()
    response = assistant.respond_to_request("   ", [], k=3)

    assert response.guardrail_message is not None
    assert "Please share" in response.guardrail_message
    assert response.confidence <= 0.2


def test_assistant_retrieves_and_explains_relevant_songs():
    assistant = MusicAssistant()
    songs = [
        {
            "id": 1,
            "title": "Sunrise City",
            "artist": "Neon Echo",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.82,
            "tempo_bpm": 118,
            "valence": 0.84,
            "danceability": 0.79,
            "acousticness": 0.18,
        },
        {
            "id": 2,
            "title": "Midnight Coding",
            "artist": "LoRoom",
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.42,
            "tempo_bpm": 78,
            "valence": 0.56,
            "danceability": 0.62,
            "acousticness": 0.71,
        },
    ]

    response = assistant.respond_to_request("I want upbeat pop songs for a happy workout", songs, k=2)

    assert response.retrieved_songs
    assert "Sunrise City" in response.answer
    assert response.confidence >= 0.5
