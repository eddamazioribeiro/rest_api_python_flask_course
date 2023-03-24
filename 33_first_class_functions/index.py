def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Divisor cannot be 0 (zero)")

  return dividend / divisor

def add(*values):
  return sum((list(values)))

def calculate(*values, operator):
  return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)

result = calculate(4, 5, 6, operator=add)
print(result)

def search(sequence, expected, finder):
  for elem in sequence:
    if finder(elem) == expected:
      return elem
  
  raise RuntimeError(f"Could not find an element with {expected}.")

def get_friend_name(friend):
  return friend["name"]

friends = [
  {"name": "Bob Smith", "age": 24},
  {"name": "Adam Paige", "age": 30},
  {"name": "Anne Spoonful", "age": 27},
]

print(search(friends, "Bob Smith", get_friend_name))
# using a lambda function
print(search(friends, "Bob Smith", lambda friend: friend["name"]))