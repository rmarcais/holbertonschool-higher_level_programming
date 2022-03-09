-- This script uses the hbtn_0d_tvshows database to list all genres of the show Dexter.
-- Lists all genres of the show Dexter.
SELECT tv_genres.name AS "name"
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter';
