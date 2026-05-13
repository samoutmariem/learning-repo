
#  Boolean values
a = True
b = False

print(a, b)
# True False


#  Logical AND
x = 10

print(x > 5 and x < 20)
# True


#  Logical OR
print(x < 5 or x == 10)
# True


#  Logical NOT
print(not (x > 5))
# False


#  Truthy / Falsy values
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hello"))  # True
print(bool([]))       # False
print(bool([1, 2]))   # True


#  Comparison + logic
age = 25

if age >= 18 and age <= 30:
    print("Young adult")
# Young adult


#  Bitwise AND (&)
a = 5   # 0101
b = 3   # 0011

print(a & b)
# 1  (0001)


#  Bitwise OR (|)
print(a | b)
# 7  (0111)


#  Bitwise XOR (^)
print(a ^ b)
# 6  (0110)


#  Bitwise NOT (~)
print(~a)
# -6


#  Left shift (<<)
x = 5   # 0101

print(x << 1)
# 10 (1010)


#  Right shift (>>)
print(x >> 1)
# 2 (0010)


#  Check even / odd using bits
num = 4

if num & 1 == 0:
    print("Even")
else:
    print("Odd")
# Even


#  Toggle bit
x = 5  # 0101

# Toggle 2nd bit
print(x ^ (1 << 1))
# 7 (0111)


#  Set a bit
x = 5  # 0101
print(x | (1 << 1))
# 7 (0111)


#  Clear a bit
x = 7  # 0111
print(x & ~(1 << 1))
# 5 (0101)


#  Check if bit is set
x = 5  # 0101

if x & (1 << 2):
    print("Bit is ON")
# Bit is ON


#  Practical example (permissions)
READ = 1     # 001
WRITE = 2    # 010
EXECUTE = 4  # 100

permissions = READ | WRITE

print(permissions)  # 3

# Check permission
if permissions & WRITE:
    print("Can write")
# Can write


# 🔹 Logical vs Bitwise difference
a = True
b = False

print(a and b)  # False (logical)
print(a & b)    # False (bitwise)


# 🔹 Combining logic + bits
x = 6  # 0110

if (x & 2) and (x > 0):
    print("Condition met")
# Condition met