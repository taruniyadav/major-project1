import zipfile
import json
import sqlite3


INTEREST_KEYWORDS = {
    "Cars": ["car", "bmw", "audi", "tesla"],
    "Gaming": ["game", "gaming", "ps5"],
    "Technology": ["tech", "ai", "coding"],
    "Fitness": ["gym", "fitness"],
    "Travel": ["travel", "trip"],
    "Music": ["music", "song"],
    "Movies": ["movie", "film"],
    "Funny": ["meme", "funny"],
}


def detect_interest_from_instagram(zip_path):

    interest_score = {k: 0 for k in INTEREST_KEYWORDS}

    with zipfile.ZipFile(zip_path, "r") as z:

        for file in z.namelist():

            if file.endswith(".json"):

                try:
                    data = json.loads(z.read(file))

                    text = json.dumps(data).lower()

                    for interest, keywords in INTEREST_KEYWORDS.items():
                        for word in keywords:
                            if word in text:
                                interest_score[interest] += 1

                except:
                    pass

    detected_interest = max(interest_score, key=interest_score.get)

    return detected_interest, interest_score


# SAVE INTEREST TO DATABASE
def save_instagram_interest(username, interest):

    conn = sqlite3.connect("emotion_learning.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO instagram_interests
    (username, interest)
    VALUES (?, ?)
    """, (username, interest))

    conn.commit()
    conn.close()
