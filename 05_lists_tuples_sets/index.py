# list
## values can be changed
## items can be accessed by subscription
l = ["Bob", "Anne", "Johson"]

# tuple
## cannot be changed
## items can be accessed by subscription
t = ("Bob", "Anne", "Johson")

# set
## items cannot be accessed by subscription
## does not keep items in order
## items inside sets are unique, no duplicates
s = {"Bob", "Anne", "Johson"}

## adding and removing items
## append: add to the end of the list
l.append("Smith")
l.remove("Bob")

print(l)

## add is diferent because since sets does not have order, there's no end to append to
s.add("Gamble")
s.add("Gamble")
s.add("Anne")

print(s)