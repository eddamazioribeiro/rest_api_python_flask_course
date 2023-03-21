friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)

print(local_friends)

local_friends = abroad.difference(friends)

print(local_friends)

group_a = {"John", "Paul"}
group_b = {"Geroge", "Ringo"}

the_beatles = group_a.union(group_b)

print(the_beatles)

science_class = {"John", "Paul", "George", "Ringo"}
math_class = {"John", "Ringo"}

both_classes = science_class.intersection(math_class)

print(both_classes)