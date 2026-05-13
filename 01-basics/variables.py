# Basic variables
name = "Mariem"   # string
age = 25          # integer
price = 19.99     # float
is_dev = True     # boolean

print(name, age, price, is_dev)
# Mariem 25 19.99 True


#  Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)
# 1 2 3


#  Same value to multiple variables
a = b = c = 0
print(a, b, c)
# 0 0 0


#  Dynamic typing
x = 10
print(x)        # 10

x = "Hello"
print(x)        # Hello


#  Type checking
x = 10
print(type(x))  # <class 'int'>


#  Type casting
x = "10"
y = int(x)
z = float(x)

print(y, z)
# 10 10.0


#  Naming variables
user_name = "Mariem"   # valid
_user = "test"         # valid
UserName = "ok"        # valid

# 2name = "no" ❌ invalid


#  Constants (by convention)
PI = 3.14
MAX_USERS = 100

print(PI, MAX_USERS)
# 3.14 100


#  Global vs Local variables
x = "global"

def test():
    x = "local"
    print(x)

test()      # local
print(x)    # global


# Global keyword
x = 10

def change():
    global x
    x = 20

change()
print(x)
# 20


# Nonlocal (advanced)
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

    inner()
    print(x)

outer()
# inner


#  Mutable vs Immutable
# Immutable
x = 10
x = 20
print(x)
# 20

# Mutable
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
# [1, 2, 3, 4]


#  Variable as reference
a = [1, 2]
b = a

b.append(3)
print(a)
# [1, 2, 3]


# Copy vs Reference
a = [1, 2]
b = a.copy()

b.append(3)

print(a)  # [1, 2]
print(b)  # [1, 2, 3]


# Deleting variables
x = 10
del x
# print(x)  error


#  None (empty variable)
x = None
print(x)
# None


#  Variable unpacking
numbers = [1, 2, 3]
a, b, c = numbers

print(a, b, c)
# 1 2 3


#  Extended unpacking
a, *b = [1, 2, 3, 4]

print(a)  # 1
print(b)  # [2, 3, 4]


#  Swapping variables
a = 1
b = 2

a, b = b, a
print(a, b)
# 2 1


#  Variables in functions
def add(x, y):
    result = x + y
    return result

print(add(3, 4))
# 7


#  *args and **kwargs
def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(1, 2, name="Mariem")
# (1, 2)
# {'name': 'Mariem'}


#  Class variables vs Instance variables
class User:
    role = "admin"   # class variable

    def __init__(self, name):
        self.name = name  # instance variable

u = User("Mariem")
print(u.name, u.role)
# Mariem admin


#  Environment variables
import os

# (example: may return None if not set)
print(os.getenv("DB_NAME"))
# None


#  Type hints (annotations)
name: str = "Mariem"
age: int = 25

print(name, age)
# Mariem 25


#  Constant with typing (advanced)
from typing import Final

PI: Final = 3.14
print(PI)
# 3.14


#  Dictionary variable (important)
user = {
    "name": "Mariem",
    "job": "Developer"
}

print(user["name"])
# Mariem