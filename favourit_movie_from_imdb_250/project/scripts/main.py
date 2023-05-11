import json , os
from datetime import datetime

# Read the movies.json file
with open(os.path.join(os.path.dirname(__file__) , "movies.json" ) , encoding="utf8") as file:
    data = json.load(file)

movies = data

# Extract desired fields and add "rank" field
processed_movies = []
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
for i, movie in enumerate(movies, start=1):
    processed_movie = {
        'rank': i,
        'title': movie['title'],
        'poster': movie['poster'],
        'year': movie['year'],
        'director': movie['director'],
        'actors': movie['actors'],
        'plot': movie['plot'],
        'created_at': current_datetime,
        'updated_at': current_datetime
    }
    processed_movies.append(processed_movie)

# Save the processed movies to a new JSON file
with open('processed_movies.json', 'w') as file:
    json.dump(processed_movies, file, indent=2)



