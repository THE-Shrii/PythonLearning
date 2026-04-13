# 1
print(10 + 5)
# Output: 15
# Explanation: Addition

# 2
print(10 - 5)
# Output: 5
# Explanation: Subtraction

# 3
print(10 * 5)
# Output: 50
# Explanation: Multiplication

# 4
print(10 / 2)
# Output: 5.0
# Explanation: Division → float

# 5
print(10 // 3)
# Output: 3
# Explanation: Floor division

# 6
print(10 % 3)
# Output: 1
# Explanation: Remainder

# 7
print(2 ** 3)
# Output: 8
# Explanation: Power

# 8
print(5 + 2 * 3)
# Output: 11
# Explanation: BODMAS (× first)

# 9
print((5 + 2) * 3)
# Output: 21
# Explanation: Brackets priority

# 10
print(10 + 5 * 2 - 3)
# Output: 17
# Explanation: Order of operations

# 11
print(10 / 3)
# Output: 3.333...
# Explanation: Float division

# 12
print(10 // 3)
# Output: 3
# Explanation: Integer division

# 13
print(10 % 4)
# Output: 2
# Explanation: Remainder

# 14
print(-10 + 5)
# Output: -5
# Explanation: Negative + positive

# 15
print(2 ** 4)
# Output: 16
# Explanation: Power

# 16
x = 10
x += 5
print(x)
# Output: 15
# Explanation: x = x + 5

# 17
x = 10
x -= 3
print(x)
# Output: 7
# Explanation: x = x - 3

# 18
x = 10
x *= 2
print(x)
# Output: 20
# Explanation: x = x * 2

# 19
x = 10
x /= 2
print(x)
# Output: 5.0
# Explanation: Division → float

# 20
x = 10
x //= 3
print(x)
# Output: 3
# Explanation: Floor assign

# 21
x = 10
x %= 3
print(x)
# Output: 1
# Explanation: Remainder assign

# 22
x = 2
x **= 3
print(x)
# Output: 8
# Explanation: Power assign

# 23
print(5 > 3)
# Output: True
# Explanation: Greater than

# 24
print(5 < 3)
# Output: False
# Explanation: Less than

# 25
print(5 == 5)
# Output: True
# Explanation: Equal

# 26
print(5 != 3)
# Output: True
# Explanation: Not equal

# 27
print(5 >= 5)
# Output: True
# Explanation: Greater or equal

# 28
print(5 <= 4)
# Output: False
# Explanation: Less or equal

# 29
print("a" == "a")
# Output: True
# Explanation: String compare

# 30
print("a" > "b")
# Output: False
# Explanation: ASCII comparison

# 31
print(10 == "10")
# Output: False
# Explanation: Different types

# 32
print(10 != "10")
# Output: True
# Explanation: Not equal types

# 33
print(5 > 3 and 2 < 4)
# Output: True
# Explanation: Both True

# 34
print(5 > 3 or 2 > 4)
# Output: True
# Explanation: One True enough

# 35
print(not (5 > 3))
# Output: False
# Explanation: True → False

# 36
print(5 > 3 > 1)
# Output: True
# Explanation: Chained comparison

# 37
print(5 > 3 > 10)
# Output: False
# Explanation: Second condition fail

# 38
print("a" in "apple")
# Output: True
# Explanation: Membership

# 39
print("b" not in "apple")
# Output: True
# Explanation: Not present

# 40
x = [1, 2, 3]
print(2 in x)
# Output: True
# Explanation: Element present

# 41
x = [1, 2, 3]
print(4 not in x)
# Output: True
# Explanation: Element not present

# 42
x = [1, 2]
y = x
print(x is y)
# Output: True
# Explanation: Same memory

# 43
x = [1, 2]
y = [1, 2]
print(x is y)
# Output: False
# Explanation: Different objects

# 44
x = [1, 2]
y = [1, 2]
print(x == y)
# Output: True
# Explanation: Values same

# 45
print(True and False or True)
# Output: True
# Explanation: AND first, then OR

# 46
print(False or False and True)
# Output: False
# Explanation: AND first → False

# 47
print((False or False) and True)
# Output: False
# Explanation: Brackets change order

# 48
print(5 and 0 or 10)
# Output: 10
# Explanation: AND → 0, OR → 10

# 49
print(0 or 5 and 10)
# Output: 10
# Explanation: AND first → 10

# 50
print(not 0)
# Output: True
# Explanation: 0 = False → not → True