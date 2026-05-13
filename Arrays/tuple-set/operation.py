# #################################################
# TUPLE PROBLEMS
# #################################################

#  Problem 1
# Find max value in tuple

nums = (10, 5, 30, 7)

print(max(nums))
# 30


#  Problem 2
# Find min value

print(min(nums))
# 5


#  Problem 3
# Sum tuple values

print(sum(nums))
# 52


#  Problem 4
# Reverse tuple

nums = (1, 2, 3, 4)

print(nums[::-1])
# (4, 3, 2, 1)


#  Problem 5
# Check if item exists

languages = ("Python", "Java", "Go")

if "Python" in languages:
    print("Found")


#  Problem 6
# Count occurrences

nums = (1, 2, 2, 3, 2)

print(nums.count(2))
# 3


# Problem 7
# Find second largest

nums = (10, 50, 20, 40)

sorted_nums = sorted(nums)

print(sorted_nums[-2])
# 40


#  Problem 8
# Tuple to dictionary

data = (("name", "Mariem"), ("age", 25))

result = dict(data)

print(result)


#  Problem 9
# Swap values

a, b = 10, 20

a, b = b, a

print(a, b)
# 20 10


#  Problem 10
# Nested tuple sum

matrix = (
    (1, 2),
    (3, 4)
)

total = 0

for row in matrix:
    for value in row:
        total += value

print(total)
# 10



# #################################################
# SET OPERATIONS
# #################################################

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


# 🔹 Union
print(a | b)
print(a.union(b))
# {1, 2, 3, 4, 5, 6}


# 🔹 Intersection
print(a & b)
print(a.intersection(b))
# {3, 4}


# 🔹 Difference
print(a - b)
# {1, 2}


# 🔹 Symmetric Difference
print(a ^ b)
# {1, 2, 5, 6}


# 🔹 Subset
x = {1, 2}

print(x.issubset(a))
# True


# 🔹 Superset
print(a.issuperset(x))
# True


# 🔹 Disjoint
c = {10, 20}

print(a.isdisjoint(c))
# True



# #################################################
# SET DSA PROBLEMS
# #################################################

# 🔹 Problem 1
# Remove duplicates

nums = [1, 2, 2, 3, 4, 4]

unique = list(set(nums))

print(unique)


# 🔹 Problem 2
# Find common elements

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = set(a) & set(b)

print(common)
# {3, 4}


# 🔹 Problem 3
# Find unique values

a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)
# {1, 2, 4, 5}


# 🔹 Problem 4
# Check duplicates in list

nums = [1, 2, 3, 2]

if len(nums) != len(set(nums)):
    print("Duplicates found")


# 🔹 Problem 5
# Character uniqueness

text = "python"

if len(text) == len(set(text)):
    print("All unique")
else:
    print("Duplicates exist")


# 🔹 Problem 6
# Count unique words

sentence = "python java python go java"

words = sentence.split()

unique_words = set(words)

print(len(unique_words))
# 3


# 🔹 Problem 7
# Find missing values

a = {1, 2, 3, 4, 5}
b = {2, 3}

missing = a - b

print(missing)
# {1, 4, 5}


# 🔹 Problem 8
# Pair matching

students_python = {"Ali", "Mariem", "Sara"}
students_java = {"Mariem", "Ahmed"}

both = students_python & students_java

print(both)
# {'Mariem'}


# 🔹 Problem 9
# Unique vowels

text = "programming"

vowels = {"a", "e", "i", "o", "u"}

found = set()

for char in text:
    if char in vowels:
        found.add(char)

print(found)


# 🔹 Problem 10
# Remove common elements

a = {1, 2, 3, 4}
b = {3, 4}

result = a - b

print(result)
# {1, 2}