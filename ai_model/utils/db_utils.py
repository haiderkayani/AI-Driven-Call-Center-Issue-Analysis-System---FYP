import psycopg2
from datetime import datetime

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
cursor = conn.cursor()

def save_to_database(audio_filename, urdu_transcription, english_translation, sentiment_label, sentiment_score):
    query = """
    INSERT INTO transcriptions (audio_filename, urdu_transcription, english_translation, sentiment_label, sentiment_score)
    VALUES (%s, %s, %s, %s, %s);
    """
    cursor.execute(query, (audio_filename, urdu_transcription, english_translation, sentiment_label, sentiment_score))
    conn.commit()
    print("Data saved to database!")

def close_connection():
    cursor.close()
    conn.close()