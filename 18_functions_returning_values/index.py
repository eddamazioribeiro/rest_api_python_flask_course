def add_numbers(x, y):
  return x + y

result = add_numbers(5, 8)
print(result)

def divide_number(dividend, divisor):
  if divisor != 0:
    return dividend / divisor
  else:
    return "Error: divisor must be different from 0 (zero)!\n"

result = divide_number(5, 2) * 2
print(result)

# in this case, divide_number will return the error message, a string, and then printed twice in the console, caused by the multiplication by 2
# is a good practice to avoid diferent types of return in the same function
result = divide_number(dividend=5, divisor=0) * 2
print(result)