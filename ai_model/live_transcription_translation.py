from datetime import datetime
from models.asr_model import transcribe_audio
from models.translation_model import translate_urdu_to_english
from models.sentiment_model import analyze_sentiment  # NEW
from analysis.issue_analysis import extract_issue_and_urgency
from utils.audio_utils import record_audio
from utils.db_utils import save_to_database, close_connection


def live_transcribe_and_translate():
    while True:
        audio_data = record_audio()
        urdu_transcription = transcribe_audio(audio_data)

        print(f"Transcription (Urdu): {urdu_transcription}")

        if urdu_transcription.strip():
            english_translation = translate_urdu_to_english(urdu_transcription)
            print(f"Translation (English): {english_translation}")

            sentiment = analyze_sentiment(english_translation)
            sentiment_label = sentiment['label']
            sentiment_score = sentiment['score']
            print(f"Sentiment: {sentiment_label} (Confidence: {sentiment_score:.4f})")

            issue_info = extract_issue_and_urgency(english_translation)
            print(f"Issue Category: {issue_info['category']}")
            print(f"Urgency Level: {issue_info['urgency']}")

            audio_filename = f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
            save_to_database(
                audio_filename,
                urdu_transcription,
                english_translation,
                sentiment_label,
                sentiment_score,
                issue_info['category'],
                issue_info['description'],
                issue_info['urgency']
            )

        cont = input("\nPress Enter to continue, or type 'exit' to quit: ")
        if cont.lower() == "exit":
            print("Exiting live demo...")
            break

if __name__ == "__main__":
    live_transcribe_and_translate()
    close_connection()
