
#  enumerate (BEST practice)
numbers = [10, 20, 30]

for i, num in enumerate(numbers):
    print(i, num)
# 0 10
# 1 20
# 2 30


#  Loop through list of dicts
users = [
    {"name": "Mariem", "age": 25},
    {"name": "Ali", "age": 30}
]

for user in users:
    print(user["name"], user["age"])
# Mariem 25
# Ali 30


#  Loop through dictionary (keys)
user = {"name": "Mariem", "age": 25}

for key in user:
    print(key)
# name
# age


#  Loop through dictionary values
for value in user.values():
    print(value)
# Mariem
# 25


#  Loop through dictionary items
for key, value in user.items():
    print(key, value)
# name Mariem
# age 25


#  Loop through set
my_set = {1, 2, 3}

for item in my_set:
    print(item)
# 1 2 3 (order not guaranteed)


# while loop
i = 0

while i < 3:
    print(i)
    i += 1
# 0 1 2


#  break
for i in range(5):
    if i == 3:
        break
    print(i)
# 0 1 2


#  continue
for i in range(5):
    if i == 2:
        continue
    print(i)
# 0 1 3 4


#  pass
for i in range(3):
    pass


#  Nested loops
for i in range(2):
    for j in range(2):
        print(i, j)
# 0 0
# 0 1
# 1 0
# 1 1


#  Loop with condition
for i in range(6):
    if i % 2 == 0:
        print(i)
# 0 2 4


#  zip (loop multiple lists)
names = ["Mariem", "Ali"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(name, age)
# Mariem 25
# Ali 30


#  reversed loop
for i in reversed(range(5)):
    print(i)
# 4 3 2 1 0


#  sorted loop
numbers = [3, 1, 4, 2]

for num in sorted(numbers):
    print(num)
# 1 2 3 4


#  List comprehension
numbers = [1, 2, 3, 4]

squared = [x**2 for x in numbers]
print(squared)
# [1, 4, 9, 16]


#  List comprehension with condition
even = [x for x in range(10) if x % 2 == 0]
print(even)
# [0, 2, 4, 6, 8]


#  Dictionary comprehension
squares = {x: x**2 for x in range(3)}
print(squares)
# {0: 0, 1: 1, 2: 4}


#  Set comprehension
unique = {x for x in [1, 1, 2, 2, 3]}
print(unique)
# {1, 2, 3}


#  Generator expression (memory efficient)
gen = (x**2 for x in range(3))

for value in gen:
    print(value)
# 0 1 4


#  Loop else
for i in range(3):
    print(i)
else:
    print("Done")
# 0 1 2
# Done


#  Practical example (sum list)
numbers = [1, 2, 3, 4]
total = 0

for num in numbers:
    total += num

print(total)
# 10


#  Practical example (find item)
numbers = [1, 2, 3, 4]

for num in numbers:
    if num == 3:
        print("Found")
        break
# Found