class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  def average_grade(self):
    return sum(self.grades) / len(self.grades)

student_a = Student("Eduardo", (90, 90, 93, 78, 56))
student_b = Student("Rolf", (89, 37, 56, 64, 91))

print(student_a.name)
print(student_a.grades)
print(student_a.average_grade())

print(student_b.name)
print(student_b.grades)
print(student_b.average_grade())