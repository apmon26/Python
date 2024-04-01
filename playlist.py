playlist = {"title": "Sunset Play", 
            "author": "AP",
            "song" : [
            {"title": " song 1", "artist": ["John"], "duration": 2.5 , "albumn": "Hello"},
            {"title": " song 2", "artist": ["Kate"], "duration": 4.2 , "albumn": "Hello"},
            {"title": " song A", "artist": ["Iran"], "duration": 3.5 , "albumn": "Hello"},
            ]}

#within the song keyword, we need to create a dictionary for the name, the artist, the album.

total_length = 0
for song in playlist["song"]:
    total_length += (song["duration"])
print(total_length)