import streamlit as st
import sqlite3

st.set_page_config(page_title="Emotion Aware Intelligent Model", layout="wide")

st.title("Emotion Aware Intelligent Model")
st.markdown("## Welcome User")

# Initialize session state navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Initialize database + default admin
conn = sqlite3.connect("emotion_learning.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

cursor.execute("SELECT * FROM users WHERE username='admin'")
if cursor.fetchone() is None:
    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        ("admin", "admin123", "admin")
    )
    conn.commit()

conn.close()

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":

    col1, col2 = st.columns(2)

    with col1:
        if st.button("ADMIN", use_container_width=True):
            st.session_state.page = "admin_login"

    with col2:
        if st.button("STUDENT", use_container_width=True):
            st.session_state.page = "student_login"

# ---------------- ADMIN LOGIN ----------------
elif st.session_state.page == "admin_login":

    st.subheader("Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = sqlite3.connect("emotion_learning.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT role FROM users WHERE username=? AND password=?",
            (username, password)
        )

        result = cursor.fetchone()
        conn.close()

        if result and result[0] == "admin":
            st.session_state.admin_logged = True
            st.switch_page("pages/admin_dashboard.py")
        else:
            st.error("Invalid Admin Credentials")

    if st.button("Back"):
        st.session_state.page = "home"

# ---------------- STUDENT LOGIN ----------------
elif st.session_state.page == "student_login":

    st.subheader("Student Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = sqlite3.connect("emotion_learning.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT role FROM users WHERE username=? AND password=?",
            (username, password)
        )

        result = cursor.fetchone()
        conn.close()

        if result and result[0] == "user":
            st.session_state.student_logged = True
            st.session_state.username = username
            st.switch_page("pages/user_dashboard.py")
        else:
            st.error("Invalid Student Credentials")

    if st.button("Back"):
        st.session_state.page = "home"
