class BookShelf:
  # def __init__(self, quantity):
  def __init__(self, *books):
    self.books = books

  def __str__(self):
    return f"Bookshelf with {len(self.books)} books."

class Book:
  def __init__(self, name):
    super().__init__()
    self.name = name

  def __str__(self):
    return f"Book {self.name}"

moby_dick = Book("Moby Dick")
the_shining = Book("The Shining")

shelf = BookShelf(moby_dick, the_shining)

print(shelf)
print(shelf.books)