friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friends_ages["Adam"])

friends_ages["Adam"] = 31

print(friends_ages["Adam"])

friends_ages["Peter"] = 45

print(friends_ages["Peter"])

friends = [
  {"name": "Rolf", "age": 24},
  {"name": "Adam", "age": 30},
  {"name": "Anne", "age": 27},
]

# accessing element and element property
print(friends[0])
print(friends[0]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
  print(f"{student}: {student_attendance[student]}%")


for student, attendance, x in student_attendance.items():
  if "Bob" in student_attendance:
    print(f"Bob: {attendance}%")
  else:
   print(f"{student}: {attendance}%")

# get values
attendance_values = student_attendance.values()
# average of values
print(sum(attendance_values) / len(attendance_values))