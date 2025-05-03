from sentiment_model import analyze_sentiment

translated_text = "My problem was not solved in any particular way but you must have tried."

sentiment = analyze_sentiment(translated_text)
print(f"Sentiment: {sentiment['label']} (Confidence: {sentiment['score']})")
