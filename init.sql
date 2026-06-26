CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    status VARCHAR(20) DEFAULT 'available'
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE issued_books (
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(id),
    user_id INT REFERENCES users(id),
    issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 
