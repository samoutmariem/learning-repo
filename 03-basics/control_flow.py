
#  Basic if
x = 10

if x > 5:
    print("x is greater than 5")
# x is greater than 5


#  if / else
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
# Minor


#  if / elif / else
score = 85

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs improvement")
# Good


#  Nested if
x = 15

if x > 10:
    if x < 20:
        print("Between 10 and 20")
# Between 10 and 20


#  Logical operators
x = 10

if x > 5 and x < 20:
    print("Between 5 and 20")

if x < 5 or x == 10:
    print("x is 10 or less than 5")

if not x == 5:
    print("x is not 5")
# Between 5 and 20
# x is 10 or less than 5
# x is not 5


#  Comparison operators
a = 5
b = 10

print(a == b)  # False
print(a != b)  # True
print(a < b)   # True
print(a > b)   # False
print(a <= b)  # True
print(a >= b)  # False


#  Ternary (short if)
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)
# Adult


#  for loop
for i in range(3):
    print(i)
# 0 1 2


#  while loop
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
for i in range(2):
    pass


#  loop else
for i in range(3):
    print(i)
else:
    print("Loop finished")
# 0 1 2
# Loop finished


#  match-case (Python 3.10+)
status = 200

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown")
# OK


#  try / except
try:
    x = int("10")
    print(x)
except ValueError:
    print("Conversion error")
# 10


#  try / except / finally
try:
    x = int("abc")
except ValueError:
    print("Error")
finally:
    print("Done")
# Error
# Done


#  raising exceptions
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")


#  assert (debugging)
x = 10
assert x > 0
# (no output, passes)


#  practical example (login check)
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")
# Login successful


#  practical example (even/odd)
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
# Odd