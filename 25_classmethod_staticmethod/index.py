class ClassTest:
  # functions inside a class wich receive self as argument is called instance methods
  def instance_method(self):
    print(f"Called instance_method of {self}")

  @classmethod
  def class_method(cls):
    print(f"Called class_method of {cls}")

  @staticmethod
  def static_method():
    print("Called static_method")

class Book:
  TYPES = ("hardcover", "paperback")

  def __init__(self, name, book_type, weight):
    self.name = name
    self.book_type = book_type
    self.weight = weight

  def __repr__(self):
    return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

  @classmethod
  def hardcover(cls, name, page_weight):
    return Book(name, Book.TYPES[0], page_weight + 100)

  @classmethod
  # using cls and Book here has the same effect
  def paperback(cls, name, page_weight):
    return cls(name, cls.TYPES[1], page_weight)

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()

print(Book.TYPES)

book = Book("Moby Dick", "hardcover", 2000)

print(book)

# using the classmethods hardcover and paperback
heavy_book = Book.hardcover("Moby Dick", 2000)
light_book = Book.paperback("Python 101", 600)

print(heavy_book)
print(light_book)
