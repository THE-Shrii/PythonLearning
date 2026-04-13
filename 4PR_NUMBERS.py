# 1
x = 10
print(type(x))
# Output: <class 'int'>
# Explanation: Integer type

# 2
x = 10.5
print(type(x))
# Output: <class 'float'>
# Explanation: Decimal value → float

# 3
x = 2 + 3j
print(type(x))
# Output: <class 'complex'>
# Explanation: Complex number (real + imaginary)

# 4
print(10 + 5)
# Output: 15
# Explanation: Addition

# 5
print(10 - 5)
# Output: 5
# Explanation: Subtraction

# 6
print(10 * 5)
# Output: 50
# Explanation: Multiplication

# 7
print(10 / 2)
# Output: 5.0
# Explanation: Division → always float

# 8
print(10 // 3)
# Output: 3
# Explanation: Floor division (integer part)

# 9
print(10 % 3)
# Output: 1
# Explanation: Remainder

# 10
print(2 ** 3)
# Output: 8
# Explanation: Power (2^3)

# 11
print(abs(-10))
# Output: 10
# Explanation: Absolute value (positive)

# 12
print(pow(2, 3))
# Output: 8
# Explanation: Power function

# 13
print(min(1, 5, 3))
# Output: 1
# Explanation: Smallest value

# 14
print(max(1, 5, 3))
# Output: 5
# Explanation: Largest value

# 15
print(round(5.6))
# Output: 6
# Explanation: Round off

# 16
print(round(5.4))
# Output: 5
# Explanation: Round down

# 17
print(10 + 5 * 2)
# Output: 20
# Explanation: BODMAS (multiplication first)

# 18
print((10 + 5) * 2)
# Output: 30
# Explanation: Brackets priority

# 19
print(10 / 3)
# Output: 3.333...
# Explanation: Float division

# 20
print(10 // 3)
# Output: 3
# Explanation: Floor division

# 21
print(float(10))
# Output: 10.0
# Explanation: int → float

# 22
print(int(10.9))
# Output: 10
# Explanation: Decimal cut (no rounding)

# 23
print(int(-10.9))
# Output: -10
# Explanation: Towards zero

# 24
print(complex(5))
# Output: (5+0j)
# Explanation: Complex form

# 25
print(complex(2, 3))
# Output: (2+3j)
# Explanation: real + imaginary

# 26
x = 10
x += 5
print(x)
# Output: 15
# Explanation: x = x + 5

# 27
x = 10
x *= 2
print(x)
# Output: 20
# Explanation: x = x * 2

# 28
x = 10
x /= 2
print(x)
# Output: 5.0
# Explanation: Division gives float

# 29
print(5 + 2.0)
# Output: 7.0
# Explanation: int + float = float

# 30
print(5 + 2j)
# Output: (5+2j)
# Explanation: int + complex

# 31
print((2 + 3j) + (1 + 1j))
# Output: (3+4j)
# Explanation: Complex addition

# 32
print((2 + 3j) * 2)
# Output: (4+6j)
# Explanation: Complex multiplication

# 33
print((2 + 3j).real)
# Output: 2.0
# Explanation: Real part

# 34
print((2 + 3j).imag)
# Output: 3.0
# Explanation: Imaginary part

# 35
print(divmod(10, 3))
# Output: (3, 1)
# Explanation: (quotient, remainder)

# 36
print(0.1 + 0.2)
# Output: 0.30000000000000004
# Explanation: Floating point precision issue

# 37
print(round(2.675, 2))
# Output: 2.67
# Explanation: Binary rounding issue

# 38
print(pow(2, 3, 5))
# Output: 3
# Explanation: (2^3) % 5

# 39
print(10 ** 0)
# Output: 1
# Explanation: Any number^0 = 1

# 40
print(0 ** 5)
# Output: 0
# Explanation: 0 power anything = 0

# 41
print(-10 // 3)
# Output: -4
# Explanation: Floor goes down (not toward zero)

# 42
print(-10 % 3)
# Output: 2
# Explanation: Remainder always positive (Python rule)

# 43
print(10 % -3)
# Output: -2
# Explanation: Sign follows divisor

# 44
print(5 / 2)
# Output: 2.5
# Explanation: Normal division

# 45
print(5 // 2)
# Output: 2
# Explanation: Floor division

# 46
print(2 ** -1)
# Output: 0.5
# Explanation: Negative power = reciprocal

# 47
print(abs(-5.5))
# Output: 5.5
# Explanation: Absolute value

# 48
print(int(True))
# Output: 1
# Explanation: True = 1

# 49
print(float(False))
# Output: 0.0
# Explanation: False = 0

# 50
print(complex(True, False))
# Output: (1+0j)
# Explanation: True=1, False=0