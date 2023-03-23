def add_numbers(x, y):
  result = x + y
  print(result)

add_numbers(1, 2)

def say_hello(name, surname):
  print(f"Hello, {name} {surname}!")

say_hello("Eduardo", "Ribeiro")
# passing named parameters, expliciting each value
say_hello(surname="Ribeiro", name="Eduardo")
# you can use both named parameter syntax and direct value, although the unmamed ones should go first in function call
say_hello("Eduardo", surname="Ribeiro")