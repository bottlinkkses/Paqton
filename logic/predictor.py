def predict_next(rounds):
    # Simple mock logic
    recent = rounds[-3:]
    if recent.count('B') >= 2:
        return {'prediction': 'B', 'confidence': 4, 'bet': 100}
    elif recent.count('S') >= 2:
        return {'prediction': 'S', 'confidence': 4, 'bet': 100}
    else:
        return {'prediction': 'Skip', 'confidence': 3, 'bet': 0}
