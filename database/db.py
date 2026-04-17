import sqlite3

def init_db():
    conn = sqlite3.connect("emotion_learning.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            face_emotion TEXT,
            face_confidence REAL,
            voice_emotion TEXT,
            voice_confidence REAL,
            text_sentiment TEXT,
            text_score REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS instagram_interests (
            username TEXT PRIMARY KEY,
            interest TEXT
        )
    """)

    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    init_db()
