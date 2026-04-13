# 1
x = int("10")
print(x)
# Output: 10
# Explanation: String → int conversion

# 2
x = float(10)
print(x)
# Output: 10.0
# Explanation: int → float

# 3
x = str(10)
print(x)
# Output: 10
# Explanation: int → string

# 4
x = bool(1)
print(x)
# Output: True
# Explanation: Non-zero = True

# 5
x = bool(0)
print(x)
# Output: False
# Explanation: Zero = False

# 6
print(int(5.9))
# Output: 5
# Explanation: Decimal cut (no rounding)

# 7
print(float("5.5"))
# Output: 5.5
# Explanation: String → float

# 8
print(str(5.5))
# Output: 5.5
# Explanation: Float → string

# 9
print(bool("Hello"))
# Output: True
# Explanation: Non-empty string = True

# 10
print(bool(""))
# Output: False
# Explanation: Empty string = False

# 11
print(int(True))
# Output: 1
# Explanation: True = 1

# 12
print(int(False))
# Output: 0
# Explanation: False = 0

# 13
print(float(True))
# Output: 1.0
# Explanation: True → 1.0

# 14
print(str(True))
# Output: True
# Explanation: Boolean → string

# 15
print(type(int("100")))
# Output: <class 'int'>
# Explanation: Converted type check

# 16
print(int("10") + 5)
# Output: 15
# Explanation: Conversion + addition

# 17
print("10" + str(5))
# Output: 105
# Explanation: String concatenation

# 18
print(float(10) + 5)
# Output: 15.0
# Explanation: int + float = float

# 19
print(int(10.9) + 1)
# Output: 11
# Explanation: 10.9 → 10, then +1

# 20
print(bool(100))
# Output: True
# Explanation: Non-zero = True

# 21
print(bool(-1))
# Output: True
# Explanation: Negative ≠ zero → True

# 22
print(bool(0.0))
# Output: False
# Explanation: Zero float = False

# 23
print(int("0010"))
# Output: 10
# Explanation: Leading zeros ignore hote hain

# 24
print(float("10") + 0.5)
# Output: 10.5
# Explanation: String → float then add

# 25
print(str(10) * 3)
# Output: 101010
# Explanation: String repeat hota hai

# 26
print(int("10") * 3)
# Output: 30
# Explanation: Numeric multiplication

# 27
print(bool("False"))
# Output: True
# Explanation: Non-empty string = True ⚠️

# 28
print(bool([]))
# Output: False
# Explanation: Empty list = False

# 29
print(bool([1]))
# Output: True
# Explanation: Non-empty list = True

# 30
print(bool(None))
# Output: False
# Explanation: None = False

# 31
print(int(float("10.5")))
# Output: 10
# Explanation: 10.5 → 10

# 32
print(str(int(5.9)))
# Output: 5
# Explanation: 5.9 → 5 → "5"

# 33
print(type(str(10)))
# Output: <class 'str'>
# Explanation: Type check

# 34
print(type(bool("Hello")))
# Output: <class 'bool'>
# Explanation: Boolean type

# 35
print(int("5") + int("5"))
# Output: 10
# Explanation: String → int then add

# 36
print(int("10") + float("5.5"))
# Output: 15.5
# Explanation: Mixed types → float result

# 37
print(str(10 + 5))
# Output: 15
# Explanation: Calculation → string

# 38
print(bool(int("0")))
# Output: False
# Explanation: 0 → False

# 39
print(bool(int("1")))
# Output: True
# Explanation: 1 → True

# 40
print(int(bool(10)))
# Output: 1
# Explanation: True → 1

# 41
print(int(bool(0)))
# Output: 0
# Explanation: False → 0

# 42
print(str(bool("")))
# Output: False
# Explanation: Empty → False → string

# 43
print(float(int(5.9)))
# Output: 5.0
# Explanation: 5.9 → 5 → 5.0

# 44
print(int("10") + int("20") + int("30"))
# Output: 60
# Explanation: All converted then add

# 45
print(str(10) + str(20) + str(30))
# Output: 102030
# Explanation: String join

# 46
print(bool("0"))
# Output: True
# Explanation: Non-empty string ⚠️ tricky

# 47
print(int("   10   "))
# Output: 10
# Explanation: Spaces ignore hote hain

# 48
print(float("   5.5 "))
# Output: 5.5
# Explanation: Spaces allowed

# 49
print(int("-10"))
# Output: -10
# Explanation: Negative string allowed

# 50
print(int("10.5"))
# Output: Error
# Explanation: Float string direct int me convert nahi hota ❌