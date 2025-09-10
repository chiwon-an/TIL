USE library_db;

SELECT
    b.title,
    a.name,
    g.genre_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN genres g ON b.genre_id = g.id;

CREATE INDEX idx_authors_name
ON authors(name);

CREATE INDEX idx_genres_name
ON genres(genre_name);


SELECT 
    b.title,
    a.name  AS author,
    g.genre_name  AS genre
FROM books AS b
INNER JOIN authors AS a ON b.author_id = a.id
INNER JOIN genres  AS g ON b.genre_id  = g.id
WHERE a.name = 'J.K. Rowling'
  AND g.genre_name = 'Fantasy';