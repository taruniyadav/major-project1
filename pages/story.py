import streamlit as st
import time
from gtts import gTTS
import base64

from emotion.image_generator import generate_image
from emotion.keyword_extractor import extract_keywords

st.set_page_config(layout="wide")

st.title("🎬 AI Story Learning")

# ---------------- CHECK ----------------

if "story_text" not in st.session_state:
    st.error("No story found")
    st.stop()

# ---------------- TEXT ----------------

text = st.session_state.story_text
interest = st.session_state.get("interest", "technology")

sentences = text.split(".")

scenes = [s.strip() for s in sentences if len(s.strip()) > 10]

placeholder = st.empty()

# ---------------- STORY LOOP ----------------

for i, scene in enumerate(scenes):

    # 🔑 keyword
    words = extract_keywords(scene)
    keyword = words[0] if words else "technology"

    # 🖼️ image
    img = generate_image(keyword, interest)

    if img:
        placeholder.image(img, width=400)

    # 🎤 voice
    file = f"scene_{i}.mp3"
    tts = gTTS(scene)
    tts.save(file)

    audio_bytes = open(file, "rb").read()
    audio_base64 = base64.b64encode(audio_bytes).decode()

    st.markdown(
        f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

    # 🕒 sync
    time.sleep(4)

# ---------------- BACK ----------------

if st.button("⬅ Back to Learning"):
    st.switch_page("pages/learning.py")
