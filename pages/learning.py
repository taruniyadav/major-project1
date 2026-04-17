import streamlit as st
import sqlite3
import cv2
import time
import spacy
import re
from gtts import gTTS

from emotion.face_emotion import detect_face_emotion_from_frame
from emotion.text_emotion import analyze_text
from emotion.adaptive_agent import generate_response, get_avatar
from emotion.keyword_extractor import extract_keywords

st.set_page_config(layout="wide")

st.title("Learning Session")

# ---------------- SESSION CHECK ----------------

if "student_logged" not in st.session_state:
    st.error("Please login as Student")
    st.stop()

# ---------------- STATES ----------------

if "current_emotion" not in st.session_state:
    st.session_state.current_emotion = "neutral"

# ---------------- LOGOUT ----------------

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")

st.markdown("---")

col1, col2 = st.columns(2)

# ---------------- CAMERA ----------------

col1.subheader("Live Emotion Detection")

run_camera = col1.checkbox("Start Camera")

frame_placeholder = col1.empty()

if run_camera:

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        emotion, confidence = detect_face_emotion_from_frame(frame)

        st.session_state.current_emotion = emotion

        cv2.putText(frame, f"{emotion}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        frame_placeholder.image(frame, channels="BGR")

# ---------------- RIGHT PANEL ----------------

col2.subheader("Intelligent Learning Agent")

emotion = st.session_state.current_emotion
avatar = get_avatar(emotion)

col2.image(avatar, width=200)
col2.write(f"Detected Emotion: {emotion}")

# ---------------- INTEREST ----------------

conn = sqlite3.connect("emotion_learning.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT interest FROM instagram_interests WHERE username=?",
    (st.session_state.username,)
)

row = cursor.fetchone()
interest = row[0] if row else "technology"

conn.close()

col2.write(f"Learning Interest: {interest}")

# ---------------- CHAT ----------------

user_text = col2.text_area("Ask something")

if col2.button("Send") and user_text.strip() != "":

    with st.spinner("Zara is thinking..."):

        sentiment, score = analyze_text(user_text)

        response = generate_response(
            face_emotion=emotion,
            text_sentiment=sentiment,
            interest=interest,
            sector=st.session_state.get("sector", "Beginner"),
            question=user_text
        )

    

        clean_text = response.replace("**ZARA 🤖**","")

# remove instruction-like sentences
        clean_text = re.sub(r"(Expand.*|Your answer.*|Now,.*)", "", clean_text)

# split properly
        sentences = re.split(r'[.!?]', clean_text)

# keep only meaningful sentences
        scenes = [s.strip() for s in sentences if len(s.strip()) > 15]

        final_text = ". ".join(scenes)


        # ✅ KEYWORDS EXTRACTED HERE
        keywords = extract_keywords(final_text)

        if len(keywords) == 0:
            keywords = ["technology"]

        # ✅ STORE EVERYTHING
        st.session_state.story_text = final_text
        st.session_state.keywords = keywords
        st.session_state.interest = interest

        # 🚀 GO TO STORY PAGE
        st.switch_page("pages/story.py")
