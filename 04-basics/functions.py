#  Basic function
def greet():
    print("Hello World")

greet()
# Hello World


#  Function with parameters
def greet_user(name):
    print("Hello", name)

greet_user("Mariem")
# Hello Mariem


#  Multiple parameters
def add(a, b):
    print(a + b)

add(5, 3)
# 8


#  Return statement
def multiply(a, b):
    return a * b

result = multiply(4, 5)

print(result)
# 20


#  Default parameter
def country(name="Tunisia"):
    print("Country:", name)

country()
# Country: Tunisia

country("France")
# Country: France


#  Keyword arguments
def student(name, age):
    print(name, age)

student(age=25, name="Mariem")
# Mariem 25


#  Arbitrary arguments (*args)
def numbers(*args):
    print(args)

numbers(1, 2, 3, 4)
# (1, 2, 3, 4)


#  Loop inside function
def show_numbers(n):
    for i in range(n):
        print(i)

show_numbers(5)
# 0 1 2 3 4


#  Condition inside function
def check_even(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

print(check_even(4))
# Even


#  Function returning multiple values
def math_operations(a, b):
    return a + b, a - b

x, y = math_operations(10, 5)

print(x)
print(y)
# 15
# 5


#  Nested function
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()
# Outer function
# Inner function


#  Lambda function
square = lambda x: x * x

print(square(5))
# 25


#  Function with list
def show_list(items):
    for item in items:
        print(item)

show_list(["Python", "Odoo", "PostgreSQL"])


# 🔹 Function with dictionary
def show_user(user):
    print(user["name"])
    print(user["age"])

person = {
    "name": "Mariem",
    "age": 25
}

show_user(person)
# Mariem
# 25


#🔹 Recursive function
def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n - 1)

countdown(3)
# 3
# 2
# 1
# Done


#  Scope example
x = 10

def test():
    x = 5
    print("Local:", x)

test()

print("Global:", x)
# Local: 5
# Global: 10


#  Using global keyword
count = 0

def increment():
    global count
    count += 1

increment()

print(count)
# 1


#  Function as argument
def hello():
    print("Hello")

def execute(func):
    func()

execute(hello)
# Hello


#  Practical example
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login success"
    return "Wrong credentials"

print(login("admin", "1234"))
# Login success


#  Docstring
def info():
    """
    This function prints information
    """
    print("Python Functions")

info()


#  Type hints
def divide(a: int, b: int) -> float:
    return a / b

print(divide(10, 2))
# 5.0


#  Anonymous function with map()
nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))

print(result)
# [2, 4, 6, 8]


#  Filter with lambda
nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, nums))

print(even)
# [2, 4, 6]


#  Function with exception handling
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 0))
# Cannot divide by zero