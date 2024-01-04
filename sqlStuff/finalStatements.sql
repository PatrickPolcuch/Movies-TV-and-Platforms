-- Create a table for the movies dataset
-- we dont have the genre or durration, should replace with rating and age rating
-- We should have a column for each streaming site, bc a movie can be on multiple sites
CREATE TABLE movies (
  movie_id INTEGER PRIMARY KEY,
  title TEXT,
  release_year INTEGER,
  duration INTEGER,
  streaming_site TEXT,
  genre TEXT
);

-- Create a table for the tv shows dataset
-- Same comment as for the movies table
CREATE TABLE tv_shows (
  tv_show_id INTEGER PRIMARY KEY,
  title TEXT,
  release_year INTEGER,
  duration INTEGER,
  streaming_site TEXT,
  genre TEXT
);

-- Create a table for the users
-- I dont think we need a watchlist_id, unless we want a seperate watchlist table for every user
CREATE TABLE users (
  user_id INTEGER PRIMARY KEY,
  name TEXT,
  watchlist_id INTEGER
);

-- Create a table for the watchlist
-- should we have a watchlist for tv shows and a watchlist for movies and then just join them when presenting to the user? cause rn we have a movie_id and tv_show_id column and one of those values is going to be null for each row
-- Is the watchlist_id the unique identifier for each row, cause that makes sense to me
CREATE TABLE watchlist (
  watchlist_id INTEGER PRIMARY KEY,
  user_id INTEGER,
  movie_id INTEGER,
  tv_show_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);


--We should load the data with a python file, I cant get this to work

-- Load the data into the table
\COPY movies FROM '/path/to/movies.csv' DELIMITER ',' CSV HEADER;
-- Load the data into the table
\COPY tv_shows FROM '/path/to/tv_shows.csv' DELIMITER ',' CSV HEADER;
-- Load the data into the table
\COPY users FROM '/path/to/users.csv' DELIMITER ',' CSV HEADER;
-- Load the data into the table
\COPY watchlist FROM '/path/to/watchlist.csv' DELIMITER ',' CSV HEADER;


-- Query 1: Display all the movies in the database
SELECT *
FROM movies;
-- Query 2: Display all the tv shows in the database
SELECT *
FROM tv_shows;
-- Query 3: Display all the users in the database
SELECT *
FROM users;
-- Query 4: Display all the items in the watchlist
SELECT *
FROM watchlist;
-- Query 5: Display all the movies in the database
SELECT *
FROM movies
WHERE streaming_site = 'netflix';
-- Query 6: Display all the tv shows in the database
SELECT *
FROM tv_shows
WHERE streaming_site = 'hulu';
-- Query 7: Display all the movies in the database
SELECT *
FROM movies
WHERE release_year >= 2010;
-- Query 8: Display all the tv shows in the database
SELECT *
FROM tv_shows
WHERE release_year < 2010;
-- Query 9: Display all the movies in the database
SELECT *
FROM movies
WHERE genre = 'comedy';
-- Query 10: Display all the tv shows in the database
SELECT *
FROM tv_shows
WHERE genre = 'drama';
-- Query 11: Display all the movies in the database
SELECT *
FROM movies
ORDER BY release_year ASC;
-- Query 12: Display all the tv shows in the database
SELECT *
FROM tv_shows
ORDER BY release_year DESC;
-- Query 13: Make a new record in the watchlist table
INSERT INTO watchlist (user_id, movie_id, tv_show_id)
VALUES (1, 1, 1);
-- Query 14: Delete a record from the watchlist table
DELETE FROM watchlist
WHERE user_id = 1
AND movie_id = 1
AND tv_show_id = 1;
-- Query 15: Update a record in the watchlist table
UPDATE watchlist
SET user_id = 2,
  movie_id = 2,
  tv_show_id = 2
WHERE user_id = 1
AND movie_id = 1
AND tv_show_id = 1;
-- Query 16: Count the number of items in the watchlist
SELECT COUNT(*)
FROM watchlist;
-- Query 17: Join the movies and tv shows tables
SELECT *
FROM movies
JOIN tv_shows
  ON movies.movie_id = tv_shows.tv_show_id;
-- Query 18: Join the movies, tv shows, and users tables
SELECT *
FROM movies
JOIN tv_shows
  ON movies.movie_id = tv_shows.tv_show_id
JOIN users
  ON users.user_id = watchlist.user_id;
-- Query 19: Join the movies, tv shows, users, and watchlist tables
SELECT *
FROM movies
JOIN tv_shows
  ON movies.movie_id = tv_shows.tv_show_id
JOIN users
  ON users.user_id = watchlist.user_id
JOIN watchlist
  ON watchlist.watchlist_id = users.watchlist_id;
-- Query 20: Select the average duration from the watchlist table
SELECT AVG(duration)
FROM watchlist;