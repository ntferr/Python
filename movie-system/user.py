from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []


    def __repr__(self):
        return  f"<User {self.name}>"


    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)


    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))


    def watched_movies(self):
        #watched = []
        #watched.append([movie for movie in self.movies if (movie.watched)])
        watched = list(filter(lambda movie: movie.watched, self.movies))

        return watched


    def save_to_file(self):
        with open(f"{self.name}.txt", 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write(f'{movie.name}, {movie.genre}, {movie.watched}\n')
    

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(',')
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))

            user = cls(username)
            user.movies = movies
            
            return user