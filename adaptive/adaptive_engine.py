from risk.risk_detector import detect_risk

def choose_learning_mode():
    if detect_risk():
        return "supportive_mode"
    else:
        return "normal_mode"
