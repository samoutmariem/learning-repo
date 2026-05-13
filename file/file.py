# #################################################
# 1. WRITE TO A FILE (OVERWRITE)
# #################################################

file = open("data.txt", "w")

file.write("Hello World\n")
file.write("Learning Python File I/O\n")

file.close()

# ⚠️ "w" mode overwrites existing content


# #################################################
# 2. READ A FILE
# #################################################

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()


# #################################################
# 3. READ LINE BY LINE
# #################################################

file = open("data.txt", "r")

for line in file:
    print(line.strip())

file.close()


# #################################################
# 4. READ ALL LINES AS LIST
# #################################################

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# #################################################
# 5. APPEND TO FILE
# #################################################

file = open("data.txt", "a")

file.write("New line added\n")

file.close()


# #################################################
# 6. WITH STATEMENT (BEST PRACTICE)
# #################################################

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# no need to close file manually


# #################################################
# 7. WRITE LIST TO FILE
# #################################################

names = ["Ali", "Mariem", "Sara"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")


# #################################################
# 8. READ FILE AND STORE IN LIST
# #################################################

with open("names.txt", "r") as file:
    names_list = [line.strip() for line in file]

print(names_list)


# #################################################
# 9. CHECK IF FILE EXISTS
# #################################################

import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")


# #################################################
# 10. DELETE FILE
# #################################################

import os

if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("File deleted")


# #################################################
# 11. RENAME FILE
# #################################################

import os

# os.rename("old.txt", "new.txt")


# #################################################
# 12. CREATE EMPTY FILE
# #################################################

open("empty.txt", "w").close()


# #################################################
# 13. PRACTICAL EXAMPLE: LOG FILE
# #################################################

def log_message(message):
    with open("log.txt", "a") as file:
        file.write(message + "\n")


log_message("System started")
log_message("User logged in")


# #################################################
# 14. COUNT LINES IN FILE
# #################################################

with open("data.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))


# #################################################
# 15. SEARCH IN FILE
# #################################################

keyword = "Python"

with open("data.txt", "r") as file:
    for line in file:
        if keyword in line:
            print("Found:", line.strip())


# #################################################
# 16. COPY FILE CONTENT
# #################################################

with open("data.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as dest:
    dest.write(content)


# #################################################
# 17. SAFE FILE HANDLING (ERROR SAFE)
# #################################################

try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")


# #################################################
# 18. CSV-LIKE SIMPLE FILE
# #################################################

data = [
    "id,name,age",
    "1,Ali,20",
    "2,Mariem,25"
]

with open("data.csv", "w") as file:
    for row in data:
        file.write(row + "\n")


# #################################################
# 19. READ CSV-LIKE FILE
# #################################################

with open("data.csv", "r") as file:
    for line in file:
        values = line.strip().split(",")
        print(values)


# #################################################
# 20. IMPORTANT MODES SUMMARY
# #################################################

# "r"  -> read
# "w"  -> write (overwrite)
# "a"  -> append
# "x"  -> create new file (error if exists)
# "rb" -> read binary
# "wb" -> write binary