import sqlite3
from emotion.instagram_interest import detect_interest_from_instagram
from emotion.instagram_interest import save_instagram_interest

# your Instagram zip
zip_path = "instagram_data.zip"

username = "taruni"   # test username

# detect interest
interest, scores = detect_interest_from_instagram(zip_path)

print("Detected Interest:", interest)
print("Scores:", scores)

# 🔥 SAVE TO DATABASE
save_instagram_interest(username, interest)

# 🔎 CHECK DATABASE

conn = sqlite3.connect("emotion_learning.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM instagram_interests")

rows = cursor.fetchall()

print("interests stored instagram_interests are:", rows)

conn.close()
