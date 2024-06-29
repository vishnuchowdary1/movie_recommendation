import requests
import logging
import json

api_key = 'ba2c64e3d26c72fa526bda21363b5ba7'

def get_movie_data():
    all_movie_data = []
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            logging.info("Connection to moviedb is successful")
            movie_data = response.json()
            all_movie_data.append(movie_data)

            for page in range(2, movie_data["total_pages"]+1):
                movie_data = requests.get(url + f"&page={page}").json()
                all_movie_data.append(movie_data)

            with open('movies.json', 'w') as file:
                json.dump(all_movie_data, file)

            return all_movie_data
    
        else:
            logging.error("Connection error while pulling movie data with requests")
    except requests.exceptions.Timeout:
        logging.info("Request for movie data timed out")

all_movies = get_movie_data()
all_movies

def get_genre_data():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}"
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            logging.info("Connection to genre data is successful")
            genre_data = response.json()

            with open('genre.json', 'w') as file:
                json.dump(genre_data, file)

            return genre_data

        else:
            logging.error("Connection error while pulling genre data with requests")
        
    except requests.exceptions.Timeout:
        logging.info("Request for genre data timed out")

# genre = get_genre_data()
# genre