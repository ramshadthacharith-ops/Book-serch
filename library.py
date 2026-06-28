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

    cur.execute(
        "INSERT INTO books (title, author) VALUES (%s, %s) RETURNING id",
        (data["title"], data["author"])
    )

    book_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "id": book_id,
        "message": "Book added successfully"
    }), 201


# SEARCH BOOKS
@app.route("/search", methods=["GET"])
def search():
    q = request.args.get("q", "")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM books WHERE title ILIKE %s OR author ILIKE %s",
        (f"%{q}%", f"%{q}%")
    )

    rows = cur.fetchall()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "title": r[1],
            "author": r[2]
        })

    cur.close()
    conn.close()

    return jsonify(result)


# ✅ ALWAYS keep this at the bottom
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )
