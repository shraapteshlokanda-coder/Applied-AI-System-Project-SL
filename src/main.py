"""Command line runner for the retrieval-based music assistant."""

from pathlib import Path

from src.assistant import MusicAssistant


def main() -> None:
    assistant = MusicAssistant(Path(__file__).resolve().parents[1] / "data" / "songs.csv")
    sample_requests = [
        "I want upbeat pop songs for a happy workout",
        "I need calm lofi tracks for studying late at night",
        "Give me something intense and energetic for a run",
    ]

    print("Music Assistant Demo")
    print("=" * 30)
    for request in sample_requests:
        response = assistant.respond_to_request(request, k=3)
        print(f"\nRequest: {request}")
        print(f"Inferred profile: {response.profile}")
        print("Assistant answer:")
        print(response.answer)
        if response.guardrail_message:
            print(f"Guardrail: {response.guardrail_message}")
        print(f"Confidence: {response.confidence:.2f}")


if __name__ == "__main__":
    main()
