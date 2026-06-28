import time
import psycopg2
import os

def get_connection():
    for i in range(10):
        try:
            return psycopg2.connect(
                host="db",
                database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD")
            )
        except Exception as e:
            print(f"DB not ready (attempt {i+1}/10): {e}")
            time.sleep(3)

    raise Exception("Database connection failed after retries")
