name = "Eduardo"

greeting = f"Hello, {name}"

print(greeting)

greeting = "Hello, {}! Today is {}"
greeting_with_name = greeting.format(name, "Friday")

print(greeting_with_name)