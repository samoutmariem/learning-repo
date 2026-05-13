#  Creating lists
numbers = [1, 2, 3, 4, 5]

print(numbers)
# [1, 2, 3, 4, 5]


#  Mixed data types
mixed = [1, "Python", True, 3.14]

print(mixed)
# [1, 'Python', True, 3.14]


#  Empty list
empty = []

print(empty)
# []


# =========================
# INDEXING
# =========================

languages = ["Python", "Java", "C++", "Go"]

print(languages[0])
# Python

print(languages[1])
# Java

print(languages[-1])
# Go

print(languages[-2])
# C++


# =========================
# SLICING
# =========================

nums = [10, 20, 30, 40, 50]

print(nums[1:4])
# [20, 30, 40]

print(nums[:3])
# [10, 20, 30]

print(nums[2:])
# [30, 40, 50]

print(nums[::-1])
# Reverse list


# =========================
# MODIFYING VALUES
# =========================

fruits = ["apple", "banana", "orange"]

fruits[1] = "grape"

print(fruits)
# ['apple', 'grape', 'orange']


# =========================
# NESTED LISTS
# =========================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

# Access nested values
print(matrix[0][0])
# 1

print(matrix[1][2])
# 6

print(matrix[2][1])
# 8


# =========================
# LOOPING THROUGH LISTS
# =========================

colors = ["red", "green", "blue"]

for color in colors:
    print(color)

# red
# green
# blue


#  Loop with index
for index, value in enumerate(colors):
    print(index, value)

# 0 red
# 1 green
# 2 blue


# =========================
# LIST METHODS
# =========================

#  append()
nums = [1, 2, 3]

nums.append(4)

print(nums)
# [1, 2, 3, 4]


# insert()
nums.insert(1, 100)

print(nums)
# [1, 100, 2, 3, 4]


#  extend()
nums.extend([5, 6])

print(nums)
# [1, 100, 2, 3, 4, 5, 6]


# remove()
nums.remove(100)

print(nums)
# [1, 2, 3, 4, 5, 6]


#  pop()
nums.pop()

print(nums)
# [1, 2, 3, 4, 5]

# Remove by index
nums.pop(1)

print(nums)
# [1, 3, 4, 5]


#  clear()
test = [1, 2, 3]

test.clear()

print(test)
# []


# =========================
# SORTING
# =========================

numbers = [5, 2, 9, 1]

numbers.sort()

print(numbers)
# [1, 2, 5, 9]


#  Reverse sorting
numbers.sort(reverse=True)

print(numbers)
# [9, 5, 2, 1]


#  sorted() function
nums = [4, 1, 7, 3]

new_nums = sorted(nums)

print(new_nums)
# [1, 3, 4, 7]


# =========================
# REVERSE
# =========================

letters = ["a", "b", "c"]

letters.reverse()

print(letters)
# ['c', 'b', 'a']


# =========================
# LENGTH
# =========================

items = ["Python", "Odoo", "PostgreSQL"]

print(len(items))
# 3


# =========================
# CHECK VALUE
# =========================

fruits = ["apple", "banana"]

print("apple" in fruits)
# True

print("orange" in fruits)
# False


# =========================
# CONCATENATION
# =========================

a = [1, 2]
b = [3, 4]

c = a + b

print(c)
# [1, 2, 3, 4]


# =========================
# REPEAT LIST
# =========================

nums = [1, 2]

print(nums * 3)
# [1, 2, 1, 2, 1, 2]


# =========================
# LIST COMPREHENSION
# =========================

squares = [x * x for x in range(5)]

print(squares)
# [0, 1, 4, 9, 16]


#  With condition
even = [x for x in range(10) if x % 2 == 0]

print(even)
# [0, 2, 4, 6, 8]


# =========================
# COPY LISTS
# =========================

original = [1, 2, 3]

copy_list = original.copy()

print(copy_list)
# [1, 2, 3]


# =========================
# COUNT & INDEX
# =========================

nums = [1, 2, 2, 3, 2]

print(nums.count(2))
# 3

print(nums.index(3))
# 3


# =========================
# PRACTICAL EXAMPLE
# =========================

cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print(cart)

cart.pop()

print(cart)

cart.insert(1, "Monitor")

print(cart)

cart.sort()

print(cart)


# =========================
# 2D LIST LOOP
# =========================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for row in matrix:
    for value in row:
        print(value)


# =========================
# COMMON ERRORS
# =========================

nums = [1, 2, 3]

# print(nums[10])
# IndexError: list index out of range


# =========================
# UNPACKING
# =========================

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

# 10
# 20
# 30