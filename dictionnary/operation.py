# #################################################
# BASIC DICTIONARY OPERATIONS
# #################################################

#  Create dictionary
user = {
    "name": "Mariem",
    "age": 25,
    "country": "Tunisia"
}

print(user)
# {'name': 'Mariem', 'age': 25, 'country': 'Tunisia'}


#  Access values
print(user["name"])
# Mariem

# safer access
print(user.get("age"))
# 25


#  Add new key
user["job"] = "Developer"

print(user)


#  Update value
user["age"] = 26

print(user)


#  Remove key
user.pop("job")

print(user)


#  Remove last item
user.popitem()


#  Keys / Values / Items
print(user.keys())
print(user.values())
print(user.items())


#  Loop dictionary
for key in user:
    print(key, user[key])


for key, value in user.items():
    print(key, value)


#  Check key exists
print("name" in user)
# True


#  Length
print(len(user))
# number of keys



# #################################################
# DICTIONARY METHODS
# #################################################

data = {"a": 1, "b": 2}

# update
data.update({"c": 3})

print(data)
# {'a': 1, 'b': 2, 'c': 3}


# setdefault
data.setdefault("d", 4)

print(data)


# copy
copy_data = data.copy()

print(copy_data)


# clear
temp = {"x": 10}

temp.clear()

print(temp)
# {}



# #################################################
# NESTED DICTIONARY
# #################################################

students = {
    "s1": {"name": "Ali", "age": 20},
    "s2": {"name": "Sara", "age": 22}
}

print(students["s1"]["name"])
# Ali


# loop nested
for sid, info in students.items():
    print(sid, info["name"], info["age"])



# #################################################
# DICTIONARY DSA PROBLEMS
# #################################################


#  Problem 1
# Frequency count

nums = [1, 2, 2, 3, 3, 3]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
# {1: 1, 2: 2, 3: 3}


#  Problem 2
# Character frequency

text = "python"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


#  Problem 3
# Find most frequent element

nums = [1, 2, 2, 3, 3, 3]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

most = max(freq, key=freq.get)

print(most)
# 3


#  Problem 4
# Two sum (very important DSA problem)

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(nums):
    diff = target - num

    if diff in seen:
        print("Found:", seen[diff], i)
        break

    seen[num] = i

# Found: 0 1


#  Problem 5
# Group words by length

words = ["cat", "hi", "python", "go"]

groups = {}

for w in words:
    length = len(w)

    if length not in groups:
        groups[length] = []

    groups[length].append(w)

print(groups)
# {3: ['cat'], 2: ['hi', 'go'], 6: ['python']}


#  Problem 6
# Remove duplicates (keep order)

nums = [1, 2, 2, 3, 1]

seen = {}
result = []

for num in nums:
    if num not in seen:
        result.append(num)
        seen[num] = True

print(result)
# [1, 2, 3]


#  Problem 7
# Merge dictionaries

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

merged = {**a, **b}

print(merged)
# {'x': 1, 'y': 3, 'z': 4}


#  Problem 8
# Count words in sentence

sentence = "python is fast and python is easy"

words = sentence.split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)


#  Problem 9
# Find missing key

data = {"a": 1, "b": 2}

if "c" not in data:
    print("Missing key c")


#  Problem 10
# Invert dictionary

data = {"a": 1, "b": 2}

inverted = {}

for k, v in data.items():
    inverted[v] = k

print(inverted)
# {1: 'a', 2: 'b'}


#  Problem 11
# Max value in dictionary

scores = {"A": 10, "B": 25, "C": 15}

best = max(scores, key=scores.get)

print(best)
# B


#  Problem 12
# Count unique values

data = {"a": 1, "b": 2, "c": 1}

unique_values = set(data.values())

print(len(unique_values))
# 2


#  Problem 13
# Filter dictionary

data = {"a": 10, "b": 5, "c": 20}

filtered = {k: v for k, v in data.items() if v > 10}

print(filtered)
# {'c': 20}


#  Problem 14
# Build dictionary from two lists

keys = ["a", "b", "c"]
values = [1, 2, 3]

result = dict(zip(keys, values))

print(result)
# {'a': 1, 'b': 2, 'c': 3}


#  Problem 15
# Count occurrences using get()

nums = [1, 1, 2, 3, 3, 3]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)