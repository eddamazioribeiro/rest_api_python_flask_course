def hello_person(name: str):
  print(f"Hello, {name}!")

hello_person("Eduardo")

def user_age_in_senconds():
  user_age = int(input("Enter your age:\n>> "))
  age_in_seconds = user_age * 365 * 24 * 60 * 60

  print(f"Your age in seconds: {age_in_seconds}")

print("\nWelcome to the Age in Seconds program!\n")
user_age_in_senconds()
print("Goodbye!")
