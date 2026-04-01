"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def _print_profile_block(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    print(f"\n{'=' * 60}")
    print(f"Profile: {name}")
    print(f"Preferences: {user_prefs}")
    print(f"{'=' * 60}\n")
    recs = recommend_songs(user_prefs, songs, k=k)
    print(f"Top {k} recommendations:\n")
    for song, score, explanation in recs:
        print(f"  {song['title']} — {song['artist']}")
        print(f"    Score: {score:.2f}")
        print(f"    Because: {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    # # Starter example profile
    # user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    # recommendations = recommend_songs(user_prefs, songs, k=5)
    
    profiles = [
        (
            "High-energy happy pop (default demo)",
            {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.85,
                "likes_acoustic": False,
            },
        ),
        (
            "Chill lofi (likes acoustic)",
            {
                "favorite_genre": "lofi",
                "favorite_mood": "chill",
                "target_energy": 0.4,
                "likes_acoustic": True,
            },
        ),
        (
            "Deep intense rock",
            {
                "favorite_genre": "rock",
                "favorite_mood": "intense",
                "target_energy": 0.95,
                "likes_acoustic": False,
            },
        ),
        (
            "Edge case: high energy + sad mood (conflicting signals)",
            {
                "favorite_genre": "pop",
                "favorite_mood": "sad",
                "target_energy": 0.9,
                "likes_acoustic": False,
            },
        ),
    ]
    # print("\nTop recommendations:\n")
    # for rec in recommendations:
    #     # You decide the structure of each returned item.
    #     # A common pattern is: (song, score, explanation)
    #     song, score, explanation = rec
    #     print(f"{song['title']} - Score: {score:.2f}")
    #     print(f"Because: {explanation}")
    #     print()
    for label, prefs in profiles:
        _print_profile_block(label, prefs, songs, k=5)


if __name__ == "__main__":
    main()
