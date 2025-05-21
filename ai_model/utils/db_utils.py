import psycopg2
from datetime import datetime

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER,
    password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
)
cursor = conn.cursor()

def save_to_database(audio_filename, urdu_transcription, english_translation,
                     sentiment_label, sentiment_score,
                     issue_category, issue_description, issue_urgency):
    # Insert into calls table
    cursor.execute(
        "INSERT INTO calls (audio_filename) VALUES (%s) RETURNING call_id;",
        (audio_filename,)
    )
    call_id = cursor.fetchone()[0]

    # Insert into transcriptions table
    cursor.execute(
        """INSERT INTO transcriptions (call_id, urdu_transcription, english_translation)
           VALUES (%s, %s, %s);""",
        (call_id, urdu_transcription, english_translation)
    )

    # Insert into sentiments table
    cursor.execute(
        """INSERT INTO sentiments (call_id, sentiment_label, sentiment_score)
           VALUES (%s, %s, %s);""",
        (call_id, sentiment_label, sentiment_score)
    )

    # 4. Insert into issues
    cursor.execute("""
        INSERT INTO issues (call_id, category, description, urgency_level)
        VALUES (%s, %s, %s, %s);
    """, (call_id, issue_category, issue_description, issue_urgency))

    conn.commit()
    print(f"Data saved to database for call_id = {call_id}")

def close_connection():
    cursor.close()
    conn.close()
