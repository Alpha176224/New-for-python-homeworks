import requests
import random

# Task 1: Weather API
def get_weather(city):
    api_key = "feb0e64b086b1b4396caff4839461bb9"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=feb0e64b086b1b4396caff4839461bb9&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found or API error.")

get_weather("Tashkent")

# Task 2: Movie Recommendation System
def get_movie_recommendation(genre):
    api_key = "8f4519421abda049629178cd5e645636"
    url = f"https://api.themoviedb.org/3/discover/movie?api_key=8f4519421abda049629178cd5e645636&with_genres={genre}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            movie = random.choice(data["results"])
            print(f"Recommended Movie: {movie['title']}")
            print(f"Overview: {movie['overview']}")
        else:
            print("No movies found for this genre.")
    else:
        print("API error.")

get_movie_recommendation("28")
