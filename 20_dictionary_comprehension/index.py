users = [
  (0, "Rolf", "121991a"),
  (1, "Adam", "adam_xyz"),
  (2, "Anne", "anne123"),
  (3, "username", "1234")
]

# the second value of each tuple above (the user name) will be used as a key for the dictionary
username_mapping = {user[1]: user for user in users}

print(username_mapping)

# simple login example

username_input = input("Enter your username:\n>> ")
password_input = input("Enter your password:\n>> ")

_, username, password = username_mapping[username_input]

if password_input == password:
  print("Successful login")
else:
  print("Unauthorized! Please, check your username and password")