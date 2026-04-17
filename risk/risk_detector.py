from trend.emotional_trend import compute_emotional_stability

def detect_risk():
    trend = compute_emotional_stability()

    if trend == "declining":
        return True
    return False
