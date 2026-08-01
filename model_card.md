# 🎧 Model Card: VibeFinder

## 1. Model Name

VibeFinder 1.1

## 2. Intended Use

VibeFinder is intended for classroom-style demonstrations and simple music discovery tasks. It helps users describe a mood or activity in natural language and then retrieve songs that fit that intent.

## 3. How the System Works

The assistant first infers a lightweight preference profile from the request, then retrieves songs from a small catalog and ranks them using the existing recommender logic. The result includes a short explanation and a confidence score so the user can understand how the system interpreted the request.

## 4. Data

The catalog contains 18 songs with labels for genre, mood, energy, valence, danceability, and acousticness. Because the dataset is small and hand-curated, it does not represent the full diversity of real-world music tastes.

## 5. Limitations and Bias

The system can over-weight obvious keywords such as “pop” or “chill,” which may cause it to miss songs that are a good fit but expressed with different language. The catalog is also narrow, so it may reflect a limited set of styles and artists. In practice, the assistant should be treated as a helpful prototype rather than a complete music recommendation engine.

## 6. Misuse and Safeguards

This system could be misused to over-personalize or reinforce narrow taste bubbles, especially if it is used without human review. To reduce that risk, the app includes guardrails for empty input, exposes confidence scores, and keeps the recommendations explainable rather than opaque. A human reviewer should still check whether the suggestions feel appropriate before treating them as final.

## 7. Reliability Observations

The system performed well for clearly phrased requests such as “upbeat workout” and “calm study,” but it was less reliable when the input was vague or contained conflicting signals. One surprise during testing was that the assistant sometimes made a reasonable recommendation even when the exact keywords did not appear in the song metadata, simply because the inferred profile was strong enough.

## 8. Collaboration with AI

I used AI assistance throughout the project to speed up implementation and testing, especially for the CLI integration and documentation. One helpful suggestion was to structure the assistant around a retrieval step plus a clear confidence score, which made the system easier to explain. One flawed suggestion was to rely too heavily on keyword overlap alone for matching; that would have been brittle, so I corrected it by combining retrieval with the existing scoring logic.

## 9. Reflection

This project showed me that AI systems are most dependable when they combine model behavior with explicit guardrails and human review. I learned that transparency, evaluation, and careful prompt design matter just as much as model choice.
