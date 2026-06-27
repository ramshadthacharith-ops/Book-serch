from flask import Flask, request, jsonify
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Library API with PostgreSQL 🚀"

# GET ALL BOOKS
@app.route("/books", methods=["GET"])
def get_books():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()

    books = []
    for r in rows:
        books.append({
            "id": r[0],
            "title": r[1],
            "author": r[2]
        })

    cur.close()
    conn.close()

    return jsonify(books)

# ADD BOOK
@app.route("/add", methods=["POST"])
def add_book():
    data = request.json

    conn = get_connection()
    cur = conn.cursor()
