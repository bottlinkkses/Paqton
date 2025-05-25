import json
from logic.predictor import predict_next

def main():
    with open('data/sample_rounds.json', 'r') as f:
        rounds = json.load(f)
    result = predict_next(rounds)
    print(f"Prediction: {result['prediction']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Bet Amount: {result['bet']} credits")

if __name__ == "__main__":
    main()
