# 1
x = 10
print(x)
# Output: 10
# Explanation: Variable x me 10 store hai, print se display hota hai

# 2
name = "Shrii"
print(name)
# Output: Shrii
# Explanation: String variable print hota hai

# 3
x = 5
y = 10
print(x, y)
# Output: 5 10
# Explanation: Comma se values space ke saath print hoti hain

# 4
x = 5
x = 10
print(x)
# Output: 10
# Explanation: Latest value overwrite karti hai

# 5
a = b = c = 5
print(a, b, c)
# Output: 5 5 5
# Explanation: Ek hi value multiple variables ko assign hui

# 6
x, y, z = 1, 2, 3
print(x, y, z)
# Output: 1 2 3
# Explanation: Multiple assignment ek line me

# 7
x = 5
y = "Hello"
print(x, y)
# Output: 5 Hello
# Explanation: Different data types print ho sakte hain

# 8
x = 10
print("Value of x is", x)
# Output: Value of x is 10
# Explanation: String + variable print

# 9
x = 10
print("x =", x)
# Output: x = 10
# Explanation: Label style printing

# 10
x = 5
y = 2
print(x + y)
# Output: 7
# Explanation: Numeric addition

# 11
x = "5"
y = "2"
print(x + y)
# Output: 52
# Explanation: String concatenation (join)

# 12
x = int("5")
y = int("2")
print(x + y)
# Output: 7
# Explanation: String → int conversion

# 13
x = 10
print(type(x))
# Output: <class 'int'>
# Explanation: Data type check

# 14
x = "Hello"
print(type(x))
# Output: <class 'str'>
# Explanation: String type

# 15
x = True
print(type(x))
# Output: <class 'bool'>
# Explanation: Boolean type

# 16
x = 5
y = 10
z = x + y
print(z)
# Output: 15
# Explanation: Addition result z me store

# 17
x = 5
y = 2.5
print(x + y)
# Output: 7.5
# Explanation: int + float = float

# 18
x = 5
y = "10"
print(str(x) + y)
# Output: 510
# Explanation: int → string, then join

# 19
x = "Hello"
y = 3
print(x * y)
# Output: HelloHelloHello
# Explanation: String repetition

# 20
x = 10
y = 3
print(x / y)
# Output: 3.333...
# Explanation: / always float result deta hai

# 21
x = 10
y = 3
print(x // y)
# Output: 3
# Explanation: Floor division (integer result)

# 22
x = 10
y = 3
print(x % y)
# Output: 1
# Explanation: Remainder

# 23
x = 2
y = 3
print(x ** y)
# Output: 8
# Explanation: Power (2^3)

# 24
x = 10
x += 5
print(x)
# Output: 15
# Explanation: x = x + 5

# 25
x = 10
x -= 3
print(x)
# Output: 7
# Explanation: x = x - 3

# 26
x = 10
x *= 2
print(x)
# Output: 20
# Explanation: x = x * 2

# 27
x = 10
x /= 2
print(x)
# Output: 5.0
# Explanation: Division gives float

# 28
x = 10
x %= 3
print(x)
# Output: 1
# Explanation: Remainder store hota hai

# 29
x = 5
y = 10
x, y = y, x
print(x, y)
# Output: 10 5
# Explanation: Values swap

# 30
a = 5
b = 5
print(a == b)
# Output: True
# Explanation: Values equal

# 31
a = 5
b = "5"
print(a == b)
# Output: False
# Explanation: Type different hai

# 32
x = "Python"
print(x[0])
# Output: P
# Explanation: Index 0 = first character

# 33
x = "Python"
print(x[-1])
# Output: n
# Explanation: -1 = last character

# 34
x = "Python"
print(len(x))
# Output: 6
# Explanation: Length count

# 35
x = "Hello"
y = "World"
print(x + " " + y)
# Output: Hello World
# Explanation: String join with space

# 36
x = 10
y = 5
print("Sum =", x + y)
# Output: Sum = 15
# Explanation: Label + calculation

# 37
x = 5
y = 2
print(x > y)
# Output: True
# Explanation: Comparison

# 38
x = 5
y = 2
print(x < y)
# Output: False
# Explanation: False condition

# 39
x = 5
y = 5
print(x >= y)
# Output: True
# Explanation: Equal allowed

# 40
x = 5
y = 5
print(x <= y)
# Output: True
# Explanation: Equal allowed

# 41
x = 5
y = 10
print(x != y)
# Output: True
# Explanation: Not equal

# 42
x = True
y = False
print(x and y)
# Output: False
# Explanation: AND me dono True hone chahiye

# 43
x = True
y = False
print(x or y)
# Output: True
# Explanation: OR me ek True enough

# 44
x = True
print(not x)
# Output: False
# Explanation: Opposite value

# 45
x = 5
print(bool(x))
# Output: True
# Explanation: Non-zero = True

# 46
x = 0
print(bool(x))
# Output: False
# Explanation: Zero = False

# 47
x = ""
print(bool(x))
# Output: False
# Explanation: Empty string = False

# 48
x = "Hello"
print(bool(x))
# Output: True
# Explanation: Non-empty string = True

# 49
x = None
print(x)
# Output: None
# Explanation: No value

# 50
x = None
print(type(x))
# Output: <class 'NoneType'>
# Explanation: Special type NoneType