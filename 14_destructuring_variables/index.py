# in this case, there's no need to explicit use brackets
x = 5, 11

# in this case, we must use brackets
x = [(5, 11)]

x, y = 5, 11
print(x, y)

t = 5, 11
x, y = t
print(x, y)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# list() is slightly different from items()
# return a list of tuples
print(list(student_attendance.items()))

for t in student_attendance.items():
  print(t)

for student, attendance in student_attendance.items():
  print(student, attendance)

people = [("Rolf", 42, "Mechanic"), ("James", 24, "Artists"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
  print(f"Name: {name}\nAge: {age}\nProfession: {profession}\n\n")

person = ("Bob", 42, "Mechanic")
# the _ (underscore) is a reserved variable used when destructuring an object wich we don't care about some of it's values
# in this case, the 42 (age) is going to be ignored
name, _, profession = person

print(name, _, profession)

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)