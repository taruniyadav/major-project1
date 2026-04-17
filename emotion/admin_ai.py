def generate_admin_analysis(
    question,
    emotion_counts,
    sentiment_counts,
    interest,
    risk
):

    dominant_emotion = emotion_counts.idxmax()
    dominant_sentiment = sentiment_counts.idxmax()

    negative_ratio = sentiment_counts.get("NEGATIVE", 0) / sentiment_counts.sum()

    # ---------------- MENTAL HEALTH LEVEL ----------------

    if negative_ratio > 0.6:
        depression_level = "High"
        score = 90
    elif negative_ratio > 0.3:
        depression_level = "Moderate"
        score = 60
    else:
        depression_level = "Low"
        score = 25

    q = question.lower()

    # ---------------- RESPONSE ----------------

    if "depress" in q:
        answer = f"Depression Risk Level: **{depression_level}**"

    elif "stress" in q:
        answer = f"Stress Indicator Level: **{risk}**"

    elif "mental" in q or "health" in q:
        answer = f"Mental Health Risk Level: **{depression_level}**"

    elif "emotion" in q:
        answer = f"Dominant Emotion Detected: **{dominant_emotion}**"

    elif "sentiment" in q:
        answer = f"Text Sentiment Trend: **{dominant_sentiment}**"

    else:
        answer = f"Student emotional behaviour suggests **{dominant_emotion}** patterns."

    # ---------------- RECOMMENDATION ----------------

    if depression_level == "High":
        recommendation = "Recommendation: Monitor emotional wellbeing and provide supportive learning environment."

    elif depression_level == "Moderate":
        recommendation = "Recommendation: Encourage engaging learning activities and reduce pressure."

    else:
        recommendation = "Recommendation: Continue adaptive learning using interest topics."

    return answer, recommendation, score
