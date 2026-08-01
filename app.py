import streamlit as st
from pathlib import Path

from src.assistant import MusicAssistant


st.set_page_config(page_title="VibeFinder", page_icon="🎵", layout="centered")
st.title("VibeFinder 🎵")
st.write("Describe a mood, activity, or vibe and I’ll suggest matching songs.")

assistant = MusicAssistant(Path(__file__).resolve().parent / "data" / "songs.csv")

request = st.text_area(
    "What kind of music are you in the mood for?",
    placeholder="Example: upbeat pop songs for a happy workout",
)

if st.button("Find songs"):
    if not request.strip():
        st.warning("Please share a short description of the mood, activity, or vibe you're looking for.")
    else:
        with st.spinner("Finding songs..."):
            response = assistant.respond_to_request(request, k=3)

        st.subheader("Inferred vibe")
        st.write(response.profile)

        st.subheader("Assistant reply")
        st.write(response.answer)

        st.subheader("Suggested songs")
        if response.retrieved_songs:
            for song in response.retrieved_songs:
                st.write(f"- {song['title']} by {song['artist']} ({song['genre']}, {song['mood']})")
        else:
            st.write("No songs matched the current request.")

        st.metric("Confidence", f"{response.confidence:.2f}")

        if response.guardrail_message:
            st.warning(response.guardrail_message)
