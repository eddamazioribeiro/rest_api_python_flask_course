movies = {"The Matrix", "2001", "The Shining"}
user_movie = input("Enter a movie you've watched recently:\n>> ")

if user_movie in movies:
  print(f"I've watched {user_movie} too!")
else:
  print("I haven't watched that yet")