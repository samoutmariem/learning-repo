# =========================
# BASIC OPERATIONS
# =========================

nums = [1, 2, 3]

# Add item
nums.append(4)

print(nums)
# [1, 2, 3, 4]


# Remove item
nums.remove(2)

print(nums)
# [1, 3, 4]


# Length
print(len(nums))
# 3


# Sum
print(sum(nums))
# 8


# Max / Min
print(max(nums))
# 4

print(min(nums))
# 1


# =========================
# PROBLEM 1
# FIND LARGEST NUMBER
# =========================

numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)
# Largest: 89


# =========================
# PROBLEM 2
# FIND SMALLEST NUMBER
# =========================

numbers = [12, 45, 7, 89, 23]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)
# Smallest: 7


# =========================
# PROBLEM 3
# COUNT EVEN NUMBERS
# =========================

nums = [1, 2, 3, 4, 5, 6]

count = 0

for num in nums:
    if num % 2 == 0:
        count += 1

print("Even numbers:", count)
# Even numbers: 3


# =========================
# PROBLEM 4
# SUM ALL NUMBERS
# =========================

nums = [10, 20, 30]

total = 0

for num in nums:
    total += num

print("Total:", total)
# Total: 60


# =========================
# PROBLEM 5
# REVERSE LIST
# =========================

nums = [1, 2, 3, 4]

reversed_list = nums[::-1]

print(reversed_list)
# [4, 3, 2, 1]


# =========================
# PROBLEM 6
# REMOVE DUPLICATES
# =========================

nums = [1, 2, 2, 3, 4, 4, 5]

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print(unique)
# [1, 2, 3, 4, 5]


# =========================
# PROBLEM 7
# SEARCH FOR VALUE
# =========================

names = ["Ali", "Mariem", "Sara"]

search = "Mariem"

if search in names:
    print("Found")
else:
    print("Not found")

# Found


# =========================
# PROBLEM 8
# SECOND LARGEST NUMBER
# =========================

nums = [10, 5, 20, 8]

nums.sort()

print(nums[-2])
# 10


# =========================
# PROBLEM 9
# MERGE LISTS
# =========================

a = [1, 2]
b = [3, 4]

merged = a + b

print(merged)
# [1, 2, 3, 4]


# =========================
# PROBLEM 10
# FIND AVERAGE
# =========================

nums = [10, 20, 30, 40]

average = sum(nums) / len(nums)

print("Average:", average)
# Average: 25.0


# =========================
# PROBLEM 11
# PALINDROME CHECK
# =========================

word = ["m", "a", "d", "a", "m"]

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# Palindrome


# =========================
# PROBLEM 12
# FIND COMMON ELEMENTS
# =========================

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for num in a:
    if num in b:
        common.append(num)

print(common)
# [3, 4]


# =========================
# PROBLEM 13
# COUNT OCCURRENCES
# =========================

nums = [1, 2, 2, 3, 2, 4]

count = nums.count(2)

print(count)
# 3


# =========================
# PROBLEM 14
# SPLIT EVEN & ODD
# =========================

nums = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)

# Even: [2, 4, 6]
# Odd: [1, 3, 5]


# =========================
# PROBLEM 15
# ROTATE LIST
# =========================

nums = [1, 2, 3, 4, 5]

rotated = nums[1:] + nums[:1]

print(rotated)
# [2, 3, 4, 5, 1]


# =========================
# PROBLEM 16
# MULTIPLY ALL VALUES
# =========================

nums = [1, 2, 3, 4]

result = 1

for num in nums:
    result *= num

print(result)
# 24


# =========================
# PROBLEM 17
# FIND INDEX
# =========================

names = ["Ali", "Mariem", "Sara"]

print(names.index("Sara"))
# 2


# =========================
# PROBLEM 18
# SORT STRINGS
# =========================

words = ["banana", "apple", "orange"]

words.sort()

print(words)
# ['apple', 'banana', 'orange']


# =========================
# PROBLEM 19
# LIST OF SQUARES
# =========================

squares = []

for i in range(1, 6):
    squares.append(i * i)

print(squares)
# [1, 4, 9, 16, 25]


# =========================
# PROBLEM 20
# MATRIX SUM
# =========================

matrix = [
    [1, 2],
    [3, 4]
]

total = 0

for row in matrix:
    for value in row:
        total += value

print(total)
# 10