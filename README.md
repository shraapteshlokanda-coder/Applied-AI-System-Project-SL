# VibeFinder: Retrieval-Based Music Assistant

## Original Project and Summary

This project builds on the original VibeFinder music recommender from Modules 1–3. It started as a content-based recommender that scored songs against a user profile, and it now includes a retrieval-based AI assistant that interprets a natural-language request, retrieves relevant songs from the catalog, and explains its suggestions with a confidence score and guardrails.

## What the System Does

VibeFinder helps a user describe a mood or activity in plain language and then suggests songs that match that intent. The assistant uses a lightweight retrieval step over the song catalog, uses a simple profile inference layer to map the request to genre, mood, energy, and acoustic preferences, and returns a short explanation for each recommendation.

## Architecture Overview

The system is organized around four main pieces:

- User input: a free-form request such as “upbeat pop songs for a workout”
- Music assistant: infers a preference profile and retrieves relevant songs
- Recommendation scorer: ranks songs from the catalog using the existing recommender logic
- Guardrails and evaluation: checks empty requests, reports confidence, and supports automated tests

The full architecture diagram is in [diagrams/architecture.md](diagrams/architecture.md).

## Setup Instructions

1. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the assistant demo:

   ```bash
   python3 -m src.main
   ```

4. Run the automated tests:

   ```bash
   pytest -q
   ```

## Sample Interactions

### Example 1: upbeat workout request

```bash
python3 -m src.main
```

```text
Request: I want upbeat pop songs for a happy workout
Inferred profile: {'favorite_genre': 'rock', 'favorite_mood': 'energetic', 'target_energy': 0.9, 'likes_acoustic': False}
Assistant answer:
I interpreted your request as a rock / energetic / energy 0.90 vibe.
- Sunrise City by Neon Echo (pop, happy)
- Rooftop Lights by Indigo Parade (indie pop, happy)
- Gym Hero by Max Pulse (pop, intense)
Confidence: 0.70
```

### Example 2: calm study request

```text
Request: I need calm lofi tracks for studying late at night
Inferred profile: {'favorite_genre': 'lofi', 'favorite_mood': 'chill', 'target_energy': 0.35, 'likes_acoustic': True}
Assistant answer:
I interpreted your request as a lofi / chill / energy 0.35 vibe.
- Midnight Coding by LoRoom (lofi, chill)
- Soft Static by Clara Vale (lofi, calm)
- Library Rain by Paper Lanterns (lofi, chill)
Confidence: 0.70
```

### Example 3: empty input guardrail

```text
Request: '   '
Guardrail: Please share a short description of the mood, activity, or vibe you're looking for so I can suggest songs.
Confidence: 0.05
```

## Design Decisions

The assistant uses a simple retrieval-first design rather than a full large-language-model pipeline because the goal is to stay reproducible and easy to test. A rule-based profile inference keeps the behavior interpretable, while the existing recommender scoring logic still powers the ranking. The trade-off is that the assistant is intentionally lightweight; it works well for this catalog but would need richer language understanding and larger data for production use.

## Testing Summary

I verified the project with automated tests and by running the CLI end to end. The suite covers empty-input guardrails and retrieval behavior, and the CLI demo shows the assistant producing different recommendations for different requests. The biggest lesson was that keyword-based retrieval is useful but can be brittle when requests are vague or use unusual phrasing.

## Reliability and Guardrails

| Test case | Expected behavior | Result |
| --- | --- | --- |
| Empty request | Return a guardrail message and low confidence | Pass |
| Upbeat workout request | Retrieve pop/happy songs | Pass |
| Calm study request | Retrieve chill/lofi songs | Pass |

## Reflection

This project taught me that AI systems are most valuable when they combine strong domain logic with a clear user experience. The recommender logic provides explainable results, while the assistant layer makes the system easier to interact with. I also learned that reliability matters as much as accuracy, because a small guardrail can prevent confusing or unhelpful outputs.



