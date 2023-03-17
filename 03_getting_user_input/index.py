user_name = input("What is your name?\n")
print(user_name)

temperature_input = input("Temperature in Celsius degrees:\n")
fahrenheit = (float(temperature_input) * 1.8) + 32
print(f"{temperature_input}ºC is {fahrenheit:.1f}ºF (Fahrenheit degrees)")