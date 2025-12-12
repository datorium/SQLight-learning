import sqlite3

conn = sqlite3.connect("Chinook.db") 
cur = conn.cursor()

query = """
SELECT artists.Name,
       AVG(tracks.Milliseconds) / 60000.0 AS avg_minutes
FROM tracks
JOIN albums  ON tracks.AlbumId = albums.AlbumId
JOIN artists ON albums.ArtistId = artists.ArtistId
GROUP BY artists.ArtistId
ORDER BY avg_minutes DESC;
"""

cur.execute(query)
rows = cur.fetchall()

for artist, avg_len in rows:
    print(f"{artist} - {avg_len:.2f} minutes")

conn.close()
