def named(name, age, **kwargs):
  print(name, age, kwargs)

details = {"name": "Bob", "age": 25}

named(**details, foo=1)

def named_args(**kwargs):
  print(kwargs)

def print_nicely(**kwargs):
  named_args(**kwargs)

  for arg, value in kwargs.items():
    print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

def both(*args, **kwargs):
  print(args)
  print(kwargs)

print(both(1, 3, 5, "foo", name="John", age=31))