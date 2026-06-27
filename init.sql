CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

INSERT INTO books (title, author) VALUES
('Linux Basics', 'John'),
('Python Guide', 'Guido'),
('DevOps Handbook', 'Kim');
