# =========================
# PYTHON MODULES & PACKAGES
# =========================


# #################################################
# 1. WHAT IS A MODULE?
# #################################################

# A module = a Python file (.py) containing functions, variables, classes


# Example: math module
import math

print(math.sqrt(16))
# 4.0

print(math.pi)
# 3.14159...


# #################################################
# 2. IMPORT SPECIFIC FUNCTION
# #################################################

from math import sqrt, pow

print(sqrt(25))
# 5.0

print(pow(2, 3))
# 8.0


# #################################################
# 3. IMPORT WITH ALIAS
# #################################################

import math as m

print(m.factorial(5))
# 120


# #################################################
# 4. RANDOM MODULE
# #################################################

import random

print(random.randint(1, 10))  # random number 1-10

print(random.choice(["A", "B", "C"]))


# #################################################
# 5. CREATE YOUR OWN MODULE
# #################################################

# Step 1: create file -> mymodule.py
# -----------------------------------
# def greet(name):
#     return "Hello " + name
# -----------------------------------


# Step 2: use it in another file

# import mymodule
# print(mymodule.greet("Mariem"))


# #################################################
# 6. IMPORT SPECIFIC FROM CUSTOM MODULE
# #################################################

# from mymodule import greet
# print(greet("Mariem"))


# #################################################
# 7. PACKAGES (FOLDER OF MODULES)
# #################################################

# Structure:
# mypackage/
# ├── __init__.py
# ├── math_utils.py
# ├── string_utils.py


# math_utils.py
# def add(a, b):
#     return a + b


# string_utils.py
# def shout(text):
#     return text.upper()


# #################################################
# 8. IMPORT FROM PACKAGE
# #################################################

# from mypackage.math_utils import add
# print(add(2, 3))


# #################################################
# 9. BUILT-IN MODULES
# #################################################

import datetime

print(datetime.datetime.now())


import os

print(os.getcwd())


# #################################################
# 10. LIST ALL FUNCTIONS IN MODULE
# #################################################

import math

print(dir(math))


# #################################################
# 11. CHECK MODULE PATH
# #################################################

import sys

print(sys.path)


# #################################################
# 12. INSTALL EXTERNAL PACKAGES (pip)
# #################################################

# Run in terminal:
# pip install requests


# #################################################
# 13. USE EXTERNAL PACKAGE
# #################################################

# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)


# #################################################
# 14. IMPORT ERROR HANDLING
# #################################################

try:
    import fake_module
except ImportError:
    print("Module not found")


# #################################################
# 15. RELOAD MODULE (ADVANCED)
# #################################################

# import importlib
# import mymodule
# importlib.reload(mymodule)


# #################################################
# 16. MAIN MODULE CHECK
# #################################################

def test():
    print("Running module")

if __name__ == "__main__":
    test()


# #################################################
# 17. COMMON BUILT-IN MODULES
# #################################################

import math      # math operations
import random    # randomness
import os        # system operations
import sys       # system info
import time      # time handling


print(time.time())