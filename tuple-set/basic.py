## #################################################
# TUPLES
# #################################################

# Creating tuples
numbers = (1, 2, 3, 4)

print(numbers)
# (1, 2, 3, 4)


#  Mixed data types
mixed = (1, "Python", True, 3.14)

print(mixed)
# (1, 'Python', True, 3.14)


#  Single item tuple
single = (5,)

print(type(single))
# <class 'tuple'>


#  Access tuple items
languages = ("Python", "Java", "Go")

print(languages[0])
# Python

print(languages[-1])
# Go


#  Tuple slicing
nums = (10, 20, 30, 40, 50)

print(nums[1:4])
# (20, 30, 40)


#  Loop through tuple
for item in languages:
    print(item)


#  Tuple length
print(len(languages))
# 3


#  Count values
nums = (1, 2, 2, 3)

print(nums.count(2))
# 2


#  Find index
print(nums.index(3))
# 3


#  Tuple unpacking
person = ("Mariem", 25, "Tunisia")

name, age, country = person

print(name)
print(age)
print(country)


#  Nested tuples
matrix = (
    (1, 2),
    (3, 4)
)

print(matrix[1][0])
# 3


#  Convert tuple to list
nums = (1, 2, 3)

nums_list = list(nums)

print(nums_list)
# [1, 2, 3]


#  Convert list to tuple
data = [4, 5, 6]

data_tuple = tuple(data)

print(data_tuple)
# (4, 5, 6)


#  Tuple concatenation
a = (1, 2)
b = (3, 4)

print(a + b)
# (1, 2, 3, 4)


#  Repeat tuple
print((1, 2) * 3)
# (1, 2, 1, 2, 1, 2)



# #################################################
# SETS
# #################################################

#  Creating sets
numbers = {1, 2, 3, 4}

print(numbers)


#  No duplicates
nums = {1, 2, 2, 3, 3}

print(nums)
# {1, 2, 3}


#  Empty set
empty = set()

print(type(empty))
# <class 'set'>


#  Add value
nums.add(5)

print(nums)


#  Remove value
nums.remove(2)

print(nums)


#  discard()
nums.discard(10)
# No error if value doesn't exist


#  pop()
nums.pop()

print(nums)


#  Clear set
test = {1, 2, 3}

test.clear()

print(test)
# set()


#  Loop through set
colors = {"red", "green", "blue"}

for color in colors:
    print(color)


#  Check value
print("red" in colors)
# True


#  Set length
print(len(colors))


#  Convert list to set
nums = [1, 2, 2, 3, 3]

unique = set(nums)

print(unique)
# {1, 2, 3}


#  Convert set to list
data = list(unique)

print(data)


#  Frozen set
frozen = frozenset([1, 2, 3])

print(frozen)


#  Nested sets using frozenset
a = frozenset([1, 2])
b = {a}

print(b)