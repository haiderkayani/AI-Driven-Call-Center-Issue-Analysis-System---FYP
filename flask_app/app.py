from flask import Flask, request, jsonify
import sys
import os

app = Flask(__name__)

# Enable CORS to allow the frontend to make API calls to the backend
from flask_cors import CORS
CORS(app)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Updated imports based on your actual file structure
from ai_model.analysis.issue_analysis import extract_issue_and_urgency
from ai_model.models.sentiment_model import analyze_sentiment
from ai_model.utils.db_utils import save_to_database

# Endpoint for submitting transcription, translation, and sentiment analysis
@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.json
    audio_filename = data['audio_filename']
    urdu_transcription = data['urdu_transcription']
    english_translation = data['english_translation']
    
    # Perform sentiment analysis
    sentiment = analyze_sentiment(english_translation)
    sentiment_label = sentiment['label']
    sentiment_score = sentiment['score']
    
    # Extract issues from the transcription
    analysis_result = extract_issue_and_urgency(english_translation)
    category = analysis_result["category"]
    urgency = analysis_result["urgency"]
    description = analysis_result["description"]
    
    # Save to database (including issues and urgency)
    save_to_database(audio_filename, urdu_transcription, english_translation, sentiment_label, sentiment_score, category, description, urgency)
    
    return jsonify({"message": "Data saved successfully", "sentiment": sentiment_label,"sentiment_score": sentiment_score,
        "issue_category": category, "urgency": urgency}), 200

# # Add any additional routes for querying or filtering the data if necessary
# @app.route('/api/queries', methods=['GET'])
# def query_data():
#     # Example: Query data from the database (filter by urgency or issue type)
#     urgency_filter = request.args.get('urgency')
#     issues_filter = request.args.get('issues')
    
#     # Logic to query the database based on filters
#     # Assume you have a function query_from_db to handle this
#     data = query_from_db(urgency_filter, issues_filter)
    
#     return jsonify(data), 200

@app.route("/get_call_data/<int:call_id>", methods=["GET"])
def get_call_data(call_id):
    cursor.execute("""
        SELECT 
            c.call_id, c.audio_filename,
            t.urdu_transcription, t.english_translation,
            s.sentiment_label, s.sentiment_score,
            i.category, i.description, i.urgency_level
        FROM calls c
        LEFT JOIN transcriptions t ON c.call_id = t.call_id
        LEFT JOIN sentiments s ON c.call_id = s.call_id
        LEFT JOIN issues i ON c.call_id = i.call_id
        WHERE c.call_id = %s;
    """, (call_id,))
    
    row = cursor.fetchone()

    if row is None:
        return jsonify({"error": "Call not found"}), 404

    data = {
        "call_id": row[0],
        "audio_filename": row[1],
        "urdu_transcription": row[2],
        "english_translation": row[3],
        "sentiment_label": row[4],
        "sentiment_score": row[5],
        "issue_category": row[6],
        "issue_description": row[7],
        "issue_urgency": row[8]
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
