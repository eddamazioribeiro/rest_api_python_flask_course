beatles = ["John", "Paul", "Ringo", "George"]
grades = [35, 60, 20, 100, 100]
grades_qty = len(grades)

for beatle in beatles:
  print(f"{beatle}")

for index in range(3):
  print(f"{beatles[index]}")


total = 0

for grade in grades:
  total += grade

print(total)

total = sum(grades)
print(total)


