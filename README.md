# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



