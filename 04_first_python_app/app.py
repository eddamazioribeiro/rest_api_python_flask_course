user_age = int(input("How old are you?\n"))
months = user_age * 12
seconds = user_age * 12 * 365 * 24 * 60 * 60
# 12 * 365 * 24 * 60 * 60
print(f"Your age, {user_age}, is equivalent to {months} months")
print(f"Your age, {user_age}, is equivalent to {seconds} seconds!")