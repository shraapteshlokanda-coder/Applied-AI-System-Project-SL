# 🎵 Music Recommender Simulation

## Project Summary

This version of the music recommender simulates how a simple content-based system can suggest songs by comparing a user’s preferred style to the features of songs in a catalog. It focuses on clear, explainable rules so the recommendations are easy to understand and adjust.

---

## How The System Works

This project uses a simple content-based recommender. It looks at the features attached to each song and compares them with a user profile that describes the kind of music a person likes. In the real world, streaming apps combine many signals such as listens, skips, playlists, and song metadata, but this simulation keeps the idea simple and transparent.

Each song is described with attributes such as genre, mood, energy, valence, and acousticness. The user profile stores a favorite genre, a favorite mood, a target energy level, and whether the user prefers acoustic songs. The recommender gives each song a score by rewarding close matches on genre, mood, and energy, while also using valence and acousticness as supporting signals.

### Algorithm Recipe

- +2.0 points for a genre match
- +1.5 points for a mood match
- +1.5 × energy similarity for closeness to the target energy
- +0.75 × valence similarity for a positive or calm vibe
- +0.5 bonus if the user likes acoustic songs and the track is highly acoustic

The songs are then ranked from highest to lowest score, and the top results are shown with an explanation.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Example output for a pop/happy/high-energy profile:

```
Loaded songs: 18

Profile: pop / happy / energy 0.8
- Sunrise City (Neon Echo) — Score: 4.15
  Reason: genre match (+2.0); mood match (+1.5); energy similarity (+0.42); valence similarity (+0.63)
- Rooftop Lights (Indigo Parade) — Score: 3.87
  Reason: mood match (+1.5); energy similarity (+0.42); valence similarity (+0.60)
- Golden Hour Pulse (Aurora Lane) — Score: 3.44
  Reason: mood match (+1.5); energy similarity (+0.33); valence similarity (+0.61)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I tested the recommender with three different user profiles:

- Pop/Happy/High-Energy: the system strongly preferred upbeat pop tracks such as Sunrise City and Gym Hero.
- Lofi/Chill/Low-Energy: the ranking shifted toward calm acoustic songs such as Midnight Coding and Library Rain.
- Rock/Intense/High-Energy: the results moved toward high-energy rock tracks like Storm Runner and Firelight Echo.

I also observed that adding valence and acousticness as supporting features helped separate songs that shared the same genre but felt different in mood. This showed that the scoring logic could produce more nuanced recommendations than a genre-only system.

---

## Limitations and Risks

This recommender is intentionally simple, so it has several limitations:

- It only works with a small catalog of songs, so it cannot capture the full diversity of real music libraries.
- It does not consider lyrics, artist identity, or listening history, which are important in real recommendation systems.
- It may over-prioritize genre and mood and miss songs that are surprisingly good matches for a user’s taste.

These limitations are discussed in more detail in the model card.

---

## Reflection

Read and complete [model_card.md](model_card.md) for a fuller explanation of the system.

This project showed me that recommender systems do not need complicated models to feel useful. Even a simple scoring rule can generate recommendations that seem reasonable when it uses the right features and gives clear explanations. I also learned that bias can appear easily in these systems, especially when the dataset is small or when one feature, such as genre, is weighted too heavily. In real-world apps, that can create filter bubbles and limit the variety of music people discover.



