# 1
print(True)
# Output: True
# Explanation: Boolean True value

# 2
print(False)
# Output: False
# Explanation: Boolean False value

# 3
print(type(True))
# Output: <class 'bool'>
# Explanation: Boolean type

# 4
print(5 > 3)
# Output: True
# Explanation: 5 greater than 3

# 5
print(5 < 3)
# Output: False
# Explanation: 5 not less than 3

# 6
print(5 == 5)
# Output: True
# Explanation: Equal values

# 7
print(5 != 5)
# Output: False
# Explanation: Not equal false

# 8
print(5 >= 3)
# Output: True
# Explanation: Greater or equal

# 9
print(5 <= 3)
# Output: False
# Explanation: Not less or equal

# 10
print(bool(1))
# Output: True
# Explanation: Non-zero = True

# 11
print(bool(0))
# Output: False
# Explanation: Zero = False

# 12
print(bool("Hello"))
# Output: True
# Explanation: Non-empty string

# 13
print(bool(""))
# Output: False
# Explanation: Empty string

# 14
print(bool([]))
# Output: False
# Explanation: Empty list

# 15
print(bool([1, 2]))
# Output: True
# Explanation: Non-empty list

# 16
print(True and False)
# Output: False
# Explanation: AND needs both True

# 17
print(True or False)
# Output: True
# Explanation: OR needs one True

# 18
print(not True)
# Output: False
# Explanation: Opposite

# 19
print(not False)
# Output: True
# Explanation: Opposite

# 20
print(5 > 3 and 2 < 1)
# Output: False
# Explanation: Second condition False

# 21
print(5 > 3 or 2 < 1)
# Output: True
# Explanation: First True enough

# 22
print(not (5 > 3))
# Output: False
# Explanation: True → False

# 23
print((5 > 3) and (2 < 4))
# Output: True
# Explanation: Both True

# 24
print((5 > 10) or (2 < 4))
# Output: True
# Explanation: Second True

# 25
print(bool(None))
# Output: False
# Explanation: None = False

# 26
print(bool(0.0))
# Output: False
# Explanation: Zero float

# 27
print(bool("False"))
# Output: True
# Explanation: String ≠ False ⚠️

# 28
print(bool({}))
# Output: False
# Explanation: Empty dict

# 29
print(bool({"a": 1}))
# Output: True
# Explanation: Non-empty dict

# 30
print(10 > 5 and 5 > 2 and 2 > 1)
# Output: True
# Explanation: All True

# 31
print(10 > 5 and 5 > 2 and 2 > 3)
# Output: False
# Explanation: Last False

# 32
print(10 > 5 or 5 > 10 or 2 > 3)
# Output: True
# Explanation: First True

# 33
print(False or False or True)
# Output: True
# Explanation: One True enough

# 34
print(False and True and True)
# Output: False
# Explanation: One False breaks AND

# 35
print(not (False or True))
# Output: False
# Explanation: True → not → False

# 36
print(5 > 3 == True)
# Output: True
# Explanation: Chaining: (5>3) and (3==True)

# 37
print(5 > 3 == False)
# Output: False
# Explanation: Second condition False

# 38
print(True == 1)
# Output: True
# Explanation: True = 1

# 39
print(False == 0)
# Output: True
# Explanation: False = 0

# 40
print(True + True)
# Output: 2
# Explanation: 1 + 1

# 41
print(False + True)
# Output: 1
# Explanation: 0 + 1

# 42
print(bool(10 > 5))
# Output: True
# Explanation: True remains True

# 43
print(bool(10 < 5))
# Output: False
# Explanation: False remains False

# 44
print(5 and 10)
# Output: 10
# Explanation: AND returns last True value

# 45
print(0 and 10)
# Output: 0
# Explanation: First False return

# 46
print(5 or 10)
# Output: 5
# Explanation: First True return

# 47
print(0 or 10)
# Output: 10
# Explanation: First True value

# 48
print("" or "Hello")
# Output: Hello
# Explanation: Empty = False → next value

# 49
print("Hi" and "Hello")
# Output: Hello
# Explanation: Both True → last return

# 50
print([] or {})
# Output: {}
# Explanation: Both False → last return