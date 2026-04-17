import streamlit as st
import sqlite3
import pandas as pd
from emotion.admin_ai import generate_admin_analysis

st.title("Admin Dashboard")

# ---------------- LOGIN CHECK ----------------

if "admin_logged" not in st.session_state:
    st.error("Please login as Admin")
    st.stop()

# ---------------- LOGOUT ----------------

if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("app.py")

# ---------------- DATABASE ----------------

conn = sqlite3.connect("emotion_learning.db")
cursor = conn.cursor()

# ---------------- ADD STUDENT ----------------

st.subheader("Add New Student")

new_user = st.text_input("Username")
new_pass = st.text_input("Password", type="password")

if st.button("Add Student"):

    try:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (new_user.lower(), new_pass, "user")
        )

        conn.commit()

        st.success("Student Added Successfully")

    except:

        st.error("User already exists")

# ---------------- REGISTERED STUDENTS ----------------

st.subheader("Registered Students")

cursor.execute("SELECT username FROM users WHERE role='user'")
users = cursor.fetchall()

for user in users:

    username = user[0]

    col1, col2 = st.columns([3,1])

    col1.write(username)

    if col2.button("View Insights", key=username):

        st.session_state.selected_student = username

# ---------------- SHOW STUDENT INSIGHTS ----------------

if "selected_student" in st.session_state:

    selected_student = st.session_state.selected_student

    st.markdown("---")

    st.header(f"Insights for {selected_student}")

    # ---------------- LOAD SESSION DATA ----------------

    df = pd.read_sql_query(
        "SELECT username, face_emotion, text_sentiment FROM sessions",
        conn
    )

    student_data = df[df["username"] == selected_student]

    if student_data.empty:

        st.warning("No session data available yet.")

    else:

        # ---------------- SESSION COUNT ----------------

        st.subheader("Session Statistics")

        st.write("Total Sessions:", len(student_data))

        # ---------------- FACE EMOTIONS ----------------

        st.subheader("Face Emotion Distribution")

        emotion_counts = student_data["face_emotion"].value_counts()

        st.bar_chart(emotion_counts)

        # ---------------- TEXT SENTIMENT ----------------

        st.subheader("Text Sentiment Distribution")

        sentiment_counts = student_data["text_sentiment"].value_counts()

        st.bar_chart(sentiment_counts)

        # ---------------- INSTAGRAM INTEREST ----------------

        cursor.execute("""
        SELECT interest
        FROM instagram_interests
        WHERE LOWER(username) = LOWER(?)
        """, (selected_student,))

        result = cursor.fetchone()

        st.subheader("Instagram Interest")

        if result:
            interest_value = result[0]
            st.success(interest_value)
        else:
            interest_value = "Unknown"
            st.info("No Instagram data uploaded")

        # ---------------- RISK LEVEL ----------------

        negative_ratio = sentiment_counts.get("NEGATIVE", 0) / len(student_data)

        if negative_ratio > 0.6:
            risk = "High"
        elif negative_ratio > 0.3:
            risk = "Moderate"
        else:
            risk = "Low"

        st.subheader("Emotional Risk Indicator")
        st.write("Risk Level:", risk)

        # ---------------- AI STUDENT ANALYSIS ----------------

        st.markdown("---")
        st.subheader("AI Student Analysis")

        admin_question = st.text_input(
            "Ask AI about this student's mental health",
            placeholder="Example: Is this student depressed?"
        )

        if st.button("Analyze Student"):

            answer, recommendation, score = generate_admin_analysis(
                admin_question,
                emotion_counts,
                sentiment_counts,
                interest_value,
                risk
            )

            # ---------------- ANSWER ----------------

            st.write(answer)

            # ---------------- RISK BAR ----------------

            st.subheader("Mental Health Risk Level")

            st.progress(score)

            # ---------------- RECOMMENDATION ----------------

            st.write(recommendation)

conn.close()
