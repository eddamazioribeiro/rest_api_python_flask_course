beatles = ["Paul", "John", "George", "Ringo", "George Martin"]
starts_with_g = [beatle for beatle in beatles if beatle.startswith("G")]

print(starts_with_g)

# same result as
starts_with_g = []

for beatle in beatles:
  if beatle.startswith("G"):
    starts_with_g.append(beatle)

print(starts_with_g)

numbers = [10, 20, 30, 100]
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

# same result as
doubled_numbers = []

for num in numbers:
  doubled_numbers.append(num * 2)

print(doubled_numbers)