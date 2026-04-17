import streamlit as st
import sqlite3
from emotion.instagram_interest import detect_interest_from_instagram
from emotion.instagram_interest import save_instagram_interest
from emotion.explainable_ai import generate_explanation, generate_voice



st.title("Student Dashboard")

# ---------------- LOGIN CHECK ----------------

if "student_logged" not in st.session_state:
    st.error("Please login as Student")
    st.stop()

# ---------------- LOGOUT ----------------

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")

st.write(f"Welcome {st.session_state.username}")

# ---------------- LEARNING SETTINGS ----------------

interest = st.selectbox(
    "Select Your Interest",
    [
        "Machine Learning",
        "Data Science",
        "Cybersecurity",
        "Web Development",
        "Cars",
        "Gaming",
        "Sports",
        "Movies",
        "Music",
        "Space",
        "Technology",
        "Business"
    ]
)

sector = st.selectbox(
    "Select Your Level",
    ["Beginner", "Intermediate", "Advanced"]
)

st.markdown("")

if st.button("Start Learning Path", use_container_width=True):
    st.session_state.interest = interest
    st.session_state.sector = sector
    st.switch_page("pages/learning.py")

# ---------------- INSTAGRAM INTEREST ----------------

conn = sqlite3.connect("emotion_learning.db")
cursor = conn.cursor()

cursor.execute("""
SELECT interest
FROM instagram_interests
WHERE username = ?
""", (st.session_state.username,))

result = cursor.fetchone()

conn.close()

st.markdown("---")
st.subheader("Instagram Interest Detection")

# ---------------- IF INTEREST EXISTS ----------------

if result:

    st.success(f"Your detected interest: {result[0]}")

# ---------------- IF INTEREST NOT FOUND ----------------

else:

    uploaded_file = st.file_uploader(
        "Upload Instagram Data (ZIP)",
        type="zip",
        key="instagram_upload"
    )

    if uploaded_file:

        with open("temp_instagram.zip", "wb") as f:
            f.write(uploaded_file.read())

        interest, scores = detect_interest_from_instagram(
            "temp_instagram.zip"
        )

        save_instagram_interest(
            st.session_state.username,
            interest
        )

        st.success(f"Detected Interest: {interest}")
