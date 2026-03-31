import streamlit as st
import os

from preprocessing.audio_extractor import extract_audio
from preprocessing.speech_to_text import transcribe_audio
from models.summarizer import summarize_text
from extraction.action_extractor import extract_action_items
from embeddings.rag_engine import create_index, query_index

st.set_page_config(page_title="AI Meeting Intelligence", layout="wide")

st.markdown("### 🚀 AI-powered Meeting Insights Platform")
st.title("🎙️ Multimodal AI Meeting Intelligence System")

# =========================
# ✅ CACHED FUNCTIONS
# =========================

@st.cache_data
def cached_transcription(audio_path):
    return transcribe_audio(audio_path)

@st.cache_data
def cached_summary(text):
    return summarize_text(text)

@st.cache_resource
def cached_index(text):
    return create_index(text)

# =========================
# FILE UPLOAD
# =========================

uploaded_file = st.file_uploader("Upload Audio/Video File", type=["mp3", "wav", "mp4"])

if uploaded_file is not None:
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{uploaded_file.name}"

    # Save file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    # =========================
    # AUDIO EXTRACTION
    # =========================
    if file_path.endswith(".mp4"):
        st.info("Extracting audio...")
        audio_path = "data/temp_audio.wav"
        extract_audio(file_path, audio_path)
    else:
        audio_path = file_path

    # =========================
    # TRANSCRIPTION (CACHED)
    # =========================
    with st.spinner("Transcribing audio... ⏳"):
        text = cached_transcription(audio_path)
        
    text = text[:3000]
    st.subheader("📜 Transcript")
    st.write(text)

    # =========================
    # SUMMARY (CACHED)
    # =========================
    with st.spinner("Generating summary..."):
        summary = cached_summary(text)

    st.subheader("📝 Summary")
    st.write(summary)

    # =========================
    # ACTION ITEMS
    # =========================
    st.subheader("📌 Action Items")
    actions = extract_action_items(text)

    if actions:
        for item in actions:
            st.write(item)
    else:
        st.write("No action items found.")

    # =========================
    # RAG INDEX (CACHE ONCE)
    # =========================
    if "index" not in st.session_state:
        with st.spinner("Preparing AI Q&A system..."):
            st.session_state.index, st.session_state.sentences = cached_index(text)

    # =========================
    # Q&A SYSTEM
    # =========================
    st.subheader("🤖 Ask Questions")

    question = st.text_input("Ask something about the meeting")

    if question:
        with st.spinner("Thinking... 🤖"):
            answer = query_index(
                st.session_state.index,
                st.session_state.sentences,
                question
            )

        st.write("### Answer:")
        st.write(answer)