import random

def detect_face_emotion_from_frame(frame):

    emotions = ["happy", "sad", "neutral", "angry"]

    emotion = random.choice(emotions)

    confidence = round(random.uniform(0.7, 0.95), 2)

    return emotion, confidence
