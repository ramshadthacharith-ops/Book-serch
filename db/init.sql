CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255)
);

INSERT INTO books (title, author) VALUES
('The Alchemist', 'Paulo Coelho'),
('1984', 'George Orwell'),
('Clean Code', 'Robert Martin'),
('Your New Book', 'New Author');
