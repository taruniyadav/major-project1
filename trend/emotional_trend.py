import sqlite3
import pandas as pd

def compute_emotional_stability():
    conn = sqlite3.connect("emotion_learning.db")
    df = pd.read_sql_query("SELECT * FROM sessions", conn)
    conn.close()

    if len(df) < 3:
        return "stable"

    negative_sessions = df[df["text_sentiment"] == "NEGATIVE"]
    ratio = len(negative_sessions) / len(df)

    if ratio > 0.6:
        return "declining"
    else:
        return "stable"
