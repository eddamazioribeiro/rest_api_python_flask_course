def multiply(*args):
  print(args)
  total = 1

  # iterating through args
  for arg in args:
    total *= arg

  return total

result = multiply(1, 3, 5)
print(result)

def add(x, y):
  return x + y

nums = [3, 5]
# destructuring an array to pass each argument separately
add(*nums)

# destructuring an dictionary
nums = {"x": 15, "y": 25}
print(add(**nums))

def apply(*args, operator):
  if operator == "*":
    return multiply(*args)
  elif operator == "+":
    return sum(args)
  else:
    return "No valid operator provided to apply()"

print(apply(1, 3, 6, 7, operator="*"))