# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This recommender is designed for classroom exploration and simple simulations of how music apps suggest songs. It is meant to suggest tracks that match a user’s stated preferences for genre, mood, and energy.

---

## 3. How the Model Works

The system compares a song’s genre, mood, energy, valence, and acousticness to a small user profile. It rewards close matches and ranks songs from highest to lowest score. The model is intentionally simple so that each recommendation can be explained in plain language.

---

## 4. Data

The catalog contains 18 songs with a mix of pop, lofi, rock, ambient, jazz, indie, soul, and electronic styles. The dataset includes mood labels and numeric features such as energy, valence, danceability, and acousticness. It is still small, so it cannot capture the full variety of human musical taste.

---

## 5. Strengths

The recommender works well for clear profiles such as “happy pop” or “chill lofi.” It is especially good at explaining why a song was chosen, because each score is built from understandable features.

---

## 6. Limitations and Bias

The system can over-prioritize genre and mood and may miss good songs that are outside those exact labels. Because the catalog is small and hand-curated, it may also reflect a narrow set of artists and styles. A user who likes unusual combinations of moods or genres may get less satisfying results.

---

## 7. Evaluation

I tested the recommender with three example profiles: pop/happy/high energy, lofi/chill/low energy, and rock/intense/high energy. The results changed in sensible ways, with upbeat songs rising for energetic profiles and calmer acoustic songs rising for chill profiles. One surprise was that energy and valence had a noticeable impact even when the genre or mood did not fully match.

---

## 8. Future Work

I would add more songs and more diverse genres, include listening history as a feature, and improve the scoring so it can handle mixed tastes more gracefully. I would also like to add more explanation detail so users can understand why one song was ranked above another.

---

## 9. Personal Reflection

This project made me realize that even a simple recommender can feel surprisingly useful when the features are chosen well. Using AI tools helped me move quickly, but I still had to verify the logic and make sure the recommendations matched the intended behavior rather than just the code output.