"""Command line runner for the music recommender simulation."""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    sample_profiles = [
        {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.8, "likes_acoustic": False},
        {"favorite_genre": "lofi", "favorite_mood": "chill", "target_energy": 0.4, "likes_acoustic": True},
        {"favorite_genre": "rock", "favorite_mood": "intense", "target_energy": 0.9, "likes_acoustic": False},
    ]

    for profile in sample_profiles:
        print(f"\nProfile: {profile['favorite_genre']} / {profile['favorite_mood']} / energy {profile['target_energy']}")
        recommendations = recommend_songs(profile, songs, k=5)
        for song, score, explanation in recommendations:
            print(f"- {song['title']} ({song['artist']}) — Score: {score:.2f}")
            print(f"  Reason: {explanation}")


if __name__ == "__main__":
    main()
