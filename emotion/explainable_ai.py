from gtts import gTTS

def generate_explanation(topic, interest):

    topic = topic.lower()

    if "supervised learning" in topic:

        if interest.lower() == "cars":

            explanation = """
Supervised learning is a machine learning method where models learn from labeled data.

For example in self-driving car technology, images of cars, pedestrians, and traffic lights
are labeled so the system learns to recognize them automatically.
"""

        else:

            explanation = """
Supervised learning is a machine learning method where models learn from labeled examples.

For example, an email system learns from labeled spam and non-spam emails to classify new messages.
"""

    else:

        explanation = "This concept will be explained using simple adaptive examples."

    return explanation


def generate_voice(text):

    tts = gTTS(text)

    file_path = "explanation.mp3"

    tts.save(file_path)

    return file_path
