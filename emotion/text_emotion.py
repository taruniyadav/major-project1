def analyze_text(text):

    text = text.lower()

    negative_words = ["sad", "bad", "depressed", "angry", "upset", "stress"]
    positive_words = ["happy", "good", "great", "excited", "love"]

    score = 0

    for word in negative_words:
        if word in text:
            score -= 1

    for word in positive_words:
        if word in text:
            score += 1

    if score < 0:
        return "NEGATIVE", abs(score)
    elif score > 0:
        return "POSITIVE", score
    else:
        return "NEUTRAL", 1
