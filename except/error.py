# #################################################
# BASIC TRY / EXCEPT
# #################################################

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output:
# Cannot divide by zero


# #################################################
# MULTIPLE EXCEPTIONS
# #################################################

try:
    num = int("hello")
except ZeroDivisionError:
    print("Math error")
except ValueError:
    print("Invalid value")

# Output:
# Invalid value


# #################################################
# GENERIC EXCEPT
# #################################################

try:
    print(undefined_variable)
except Exception as e:
    print("Error happened:", e)


# #################################################
# ELSE BLOCK
# #################################################

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("No error, result =", x)

# Output:
# No error, result = 5.0


# #################################################
# FINALLY BLOCK
# #################################################

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error occurred")
finally:
    print("This always runs")

# Output:
# Error occurred
# This always runs


# #################################################
# USER INPUT SAFETY
# #################################################

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Please enter a valid number")


# #################################################
# FILE ERROR HANDLING
# #################################################

try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found")


# #################################################
# MULTIPLE EXCEPT IN ONE LINE
# #################################################

try:
    x = int("abc")
except (ValueError, TypeError):
    print("Type or Value error")


# #################################################
# RAISE CUSTOM ERROR
# #################################################

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")


# #################################################
# CUSTOM EXCEPTION HANDLING FLOW
# #################################################

def check_age(age):
    if age < 18:
        raise Exception("Not allowed")
    return "Allowed"

try:
    print(check_age(16))
except Exception as e:
    print("Blocked:", e)


# #################################################
# ASSERT STATEMENT
# #################################################

x = 10

assert x > 5  # OK

# assert x < 5  # This will crash the program


# #################################################
# COMMON REAL CASE EXAMPLE
# #################################################

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide"

print(divide(10, 2))
print(divide(10, 0))


# #################################################
# LOOP WITH ERROR HANDLING
# #################################################

values = ["10", "20", "abc", "30"]

for v in values:
    try:
        print(int(v))
    except ValueError:
        print("Skipping invalid value:", v)


# #################################################
# MULTIPLE ERROR TYPES HANDLING
# #################################################

try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("Index out of range")
except Exception as e:
    print("General error:", e)


# #################################################
# BEST PRACTICE EXAMPLE
# #################################################

def safe_input():
    while True:
        try:
            return int(input("Enter number: "))
        except ValueError:
            print("Try again!")

# num = safe_input()
# print(num)


# #################################################
# FILE SAFE OPENING (BEST PRACTICE)
# #################################################

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist")