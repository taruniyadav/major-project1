import ollama
import os

os.environ["OLLAMA_NUM_PARALLEL"] = "1"


def get_avatar(face_emotion):

    if face_emotion == "happy":
        return "assets/avatars/boy_cheerful.png"
    elif face_emotion == "sad":
        return "assets/avatars/boy_sad.png"
    elif face_emotion == "fear":
        return "assets/avatars/boy_confused.png"
    elif face_emotion == "angry":
        return "assets/avatars/boy_confused.png"
    else:
        return "assets/avatars/boy_neutral.png"


def generate_response(face_emotion, text_sentiment, interest, sector, question):

    # Emotion tone
    if face_emotion in ["sad", "fear", "angry"]:
        emotion_instruction = "The student seems frustrated or sad. Respond calmly, gently, and encourage learning."
    elif face_emotion == "happy":
        emotion_instruction = "The student seems happy and motivated. Encourage curiosity."
    else:
        emotion_instruction = "The student is neutral. Keep explanation clear and engaging."

    # Difficulty level
    if sector == "Beginner":
        level_instruction = "Explain the concept in very simple terms like teaching a beginner."
    elif sector == "Intermediate":
        level_instruction = "Explain with examples and simple reasoning."
    else:
        level_instruction = "Explain with deeper technical understanding and real-world context."

    # Interest adaptation
    interest_instruction = f"""
Adapt the explanation using examples related to {interest}.
If possible, relate the concept to {interest} so the student finds it interesting.
"""

    # Final AI prompt
    prompt = f"""
You are Zara, an intelligent AI learning assistant.

IMPORTANT:
First 2 lines MUST react to student's emotion.

If student is sad:
Say something supportive like:
"You seem a bit low today... don't worry, I'll help you step by step."

If happy:
Encourage enthusiasm.

Then explain the concept.

Student Info:
Emotion: {face_emotion}
Sentiment: {text_sentiment}
Interest: {interest}
Level: {sector}

Keep response under 80 words.

Question:
{question}
"""

    try:
        response = ollama.chat(
            model="phi3:mini",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response['message']['content']

    except:
        content = "Let's learn this step by step in a simple way."

    return f"**ZARA 🤖**\n\n{content}"
