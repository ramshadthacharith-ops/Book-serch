from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host="db",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

# Home
@app.route("/")
def home():
    return "Library API is running"

# GET all books
@app.route("/books", methods=["GET"])
def get_books():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM books")
    data = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(data)

# POST - Add book
@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO books (title, author, status) VALUES (%s, %s, %s)",
        (data["title"], data["author"], "available")
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Book added successfully"}

# PUT - Update book
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "UPDATE books SET title=%s, author=%s, status=%s WHERE id=%s",
        (data["title"], data["author"], data["status"], id)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Book updated successfully"}

# DELETE - Remove book
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM books WHERE id=%s", (id,))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Book deleted successfully"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)