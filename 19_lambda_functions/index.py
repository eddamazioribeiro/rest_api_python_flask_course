def add(x, y):
  return x + y

lambda x, y: x + y
add_lambda = lambda x, y: x + y

print(add_lambda(10, 2))

# another way to call the lambda function, right after defining it
print((lambda x, y: x + y)(10, 4))

# different ways
numbers = [1, 3, 5, 9]
doubled = [x * 2 for x in numbers]
print(doubled)

def double(x):
  return x * 2

doubled = [double(x) for x in numbers]
print(doubled)

doubled = list(map(double, numbers))
print(doubled)

doubled = [(lambda x: x * 2)(x) for x in numbers]
print(doubled)



