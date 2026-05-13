#Basic print
print("Hello World")  #Hello World

#Printing multiple values
name = "Mariem"
age = 25

print(name, age) #Mariem 25

#Using separators (sep)
print("Python", "Odoo", "Dev", sep=" - ") #Python - Odoo - Dev

#Changing line ending (end)
print("Hello", end=" ")
print("World") #Hello World

#String formatting
name = "Mariem"
print(f"My name is {name}") #My name is Mariem

#.format()
print("My name is {}".format(name))#My name is Mariem

#Old % formatting
print("My name is %s" % name)#My name is Mariem

#Printing variables inside text
x = 10
y = 5
print(f"{x} + {y} = {x+y}") #10 + 5 = 15

#Printing special characters
print("Line1\nLine2")   # line1
                        # line2
print("Tab\tSpace")     # Tab     Space

#Printing quotes
print("She said 'Hello'") #She said 'Hello'
print('He said "Hi"') #He said "Hi"

#9. Printing raw text
print(r"C:\Users\Mariem\Desktop") #C:\Users\Mariem\Desktop

my_list = [1, 2, 3] 
print(my_list) #[1, 2, 3]

my_dict = {"name": "Mariem", "job": "Developer"}
print(my_dict) #{'name': 'Mariem', 'job': 'Developer'}

#Pretty printing

from pprint import pprint

data = {"name": "Mariem", "skills": ["Python", "Odoo", "API"]} 
pprint(data) #{'name': 'Mariem', 'skills': ['Python', 'Odoo', 'API']}
 
#Printing to a file
with open("output.txt", "w") as f:
    print("Hello file", file=f)

#Printing without newline
for i in range(5):
    print(i, end=" ")
#Printing formatted numbers
price = 12.3456
print(f"{price:.2f}") 
#0 1 2 3 4 12.35

#Aligning text
print(f"{'Name':<10} {'Age':>5}")  #Name         Age
print(f"{'Mariem':<10} {25:>5}")  #Mariem        25

#Debug printing
x = 10
print(f"{x=}")   #x=10

#Colored print
print("\033[91mThis is red text\033[0m") #This is red text (red color)
#or
#pip install colorama
from colorama import Fore
print(Fore.RED + "Error") #ERROR (red)

#Printing with flush (real-time output)
import time

for i in range(5):
    print(i, flush=True)
    time.sleep(1)
#0
# 1
# 2
# 3
# 4    
#Printing ASCII / Unicode
print(ord('A'))   # 65
print(chr(65))    # A

#Printing binary / hex
x = 10
print(bin(x))  # 0b1010
print(hex(x))  # 0xa

#Multi-line print
print("""
Hello
This is
Multi-line
""")
#Logging instead of print
import logging

logging.warning("This is a warning")
