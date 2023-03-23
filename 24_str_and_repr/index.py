class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    # special method, called when trying to print() a class
    def __str__(self):
      return f"Person {self.name}, {self.age} years old"

    # special method, called when debugging a class
    def __repr__(self):
      return f"<Person({self.name}, {self.age})>"
 

bob = Person("Bob", 35)
print(bob)
print(bob.__repr__())