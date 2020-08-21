from user import User


#with open('my_file.txt', 'w') as f:
#    f.write('Hello World!')
#with open('my_file.txt', 'r') as f:
#    print(f.readline())

#user = User("Nathan")

#user.add_movie("The Matrix", "Sci-fi")
#user.add_movie("The Interview", "Comedy")

#user.save_to_file()

user = User.load_from_file("Nathan.txt")
print(user.name)
print(user.movies)