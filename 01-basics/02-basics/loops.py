# Basic if
x = 10

if x > 5:
    print("x is greater than 5")
# x is greater than 5


#  if / else
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
# Adult


#  if / elif / else
score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs improvement")
# Good


#  Nested if
x = 10

if x > 5:
    if x < 20:
        print("x is between 5 and 20")
# x is between 5 and 20


#  Logical operators
x = 10

if x > 5 and x < 20:
    print("Between 5 and 20")

if x < 5 or x == 10:
    print("x is 10 or less than 5")
# Between 5 and 20
# x is 10 or less than 5


#  for loop (basic)
for i in range(5):
    print(i)
# 0 1 2 3 4


#  for loop with list
names = ["Mariem", "Ali", "Sara"]

for name in names:
    print(name)
# Mariem
# Ali
# Sara


#  for loop with index
names = ["Mariem", "Ali"]

for i in range(len(names)):
    print(i, names[i])
# 0 Mariem
# 1 Ali


#  enumerate (better way)
names = ["Mariem", "Ali"]

for i, name in enumerate(names):
    print(i, name)
# 0 Mariem
# 1 Ali


#  while loop
i = 0

while i < 5:
    print(i)
    i += 1
# 0 1 2 3 4


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


#  pass (do nothing)
for i in range(3):
    pass  # placeholder


#  loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished")
# 0 1 2
# Loop finished


#  nested loops
for i in range(3):
    for j in range(2):
        print(i, j)
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1


#  condition inside loop
for i in range(5):
    if i % 2 == 0:
        print(f"{i} is even")
# 0 is even
# 2 is even
# 4 is even


#  simple mini example
for i in range(1, 6):
    if i == 3:
        print("Skip 3")
        continue
    print(i)
# 1
# 2
# Skip 3
# 4
# 5