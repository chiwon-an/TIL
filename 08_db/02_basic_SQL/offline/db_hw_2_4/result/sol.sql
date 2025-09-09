-- Active: 1755826251214@@127.0.0.1@3306@libraries
USE libraries;

UPDATE
    books
SET
    price = 12.99
WHERE
    isbn = '9780743273565';

UPDATE
    books
SET
    genre = 'Science Fiction'
WHERE
    isbn = '9780451524935';

UPDATE
    books
SET
    genre = "Charles Scribner's Sons"
WHERE
    isbn = '9780743273565';

SELECT * FROM books;