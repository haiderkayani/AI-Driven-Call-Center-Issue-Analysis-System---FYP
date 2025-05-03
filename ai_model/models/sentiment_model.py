# sentiment_model.py

from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

# Mapping of model labels to human-readable sentiment
label_map = {
    "LABEL_0": "NEGATIVE",
    "LABEL_1": "NEUTRAL",
    "LABEL_2": "POSITIVE"
}

def analyze_sentiment(text):
    if not text or not isinstance(text, str):
        return {"label": "INVALID_INPUT", "score": 0.0}

    result = sentiment_pipeline(text)[0]
    readable_label = label_map.get(result["label"], result["label"])

    return {
        "label": readable_label,
        "score": round(result["score"], 4)
    }
