import json
import os
from user import User


def menu():
    name = input('Enter your name: ')
    filename = f"{name}.txt"
    
    if file_exist(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie, 's' to see a list of movies," 
                "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies"
                ", 'f' to save and 'q' and quit: ")
    
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input('Enter the movie name: ')
            movie_genre = input('Enter the movie genre: ')
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print(f"Name: {movie.name}, Genre: {movie.genre}, Watched: {movie.watched}")
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
        elif user_input == 'l':
            for movie in user.watched_movies():
                print(f"Name: {movie.name}, Genre: {movie.genre}, Watched: {movie.watched}")
        elif user_input == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)
        elif user_input == 'q':
            break

        user_input = input("Enter 'a' to add a movie, 's' to see a list of movies," 
                "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies"
                ", 'f' to save and 'q' and quit: ")
    

def file_exist(filename):
    return os.path.isfile(filename)


menu()