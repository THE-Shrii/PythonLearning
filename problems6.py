# =========================================================
# 🐍 PRACTICE SET: CONDITIONAL EXPRESSIONS (20 QUESTIONS)
# =========================================================


# =========================================================
# 📌 Q1: Check Positive, Negative or Zero
# =========================================================

num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Output:
# Negative


# =========================================================
# 📌 Q2: Even or Odd
# =========================================================

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output:
# Odd


# =========================================================
# 📌 Q3: Largest of Two Numbers
# =========================================================

a = 10
b = 20

if a > b:
    print("A is largest")
else:
    print("B is largest")

# Output:
# B is largest


# =========================================================
# 📌 Q4: Largest of Three Numbers
# =========================================================

a, b, c = 5, 8, 3

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

# Output:
# 8


# =========================================================
# 📌 Q5: Check Leap Year
# =========================================================

year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# Output:
# Leap Year


# =========================================================
# 📌 Q6: Grade System
# =========================================================

marks = 65

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

# Output:
# C


# =========================================================
# 📌 Q7: Check Vowel or Consonant
# =========================================================

ch = 'a'

if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")

# Output:
# Vowel


# =========================================================
# 📌 Q8: Check Divisible by 5 and 11
# =========================================================

num = 55

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both")
else:
    print("Not divisible")

# Output:
# Divisible by both


# =========================================================
# 📌 Q9: Check Age for Voting
# =========================================================

age = 17

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Output:
# Not Eligible


# =========================================================
# 📌 Q10: Temperature Category
# =========================================================

temp = 30

if temp > 40:
    print("Very Hot")
elif temp > 25:
    print("Warm")
else:
    print("Cold")

# Output:
# Warm


# =========================================================
# 📌 Q11: Check Character Type
# =========================================================

ch = 'A'

if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")

# Output:
# Alphabet


# =========================================================
# 📌 Q12: Simple Calculator
# =========================================================

a = 10
b = 5
op = '+'

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)

# Output:
# 15


# =========================================================
# 📌 Q13: Check Pass or Fail
# =========================================================

marks = 33

if marks >= 33:
    print("Pass")
else:
    print("Fail")

# Output:
# Pass


# =========================================================
# 📌 Q14: Check Number is Multiple of 3
# =========================================================

num = 9

if num % 3 == 0:
    print("Multiple of 3")
else:
    print("Not multiple")

# Output:
# Multiple of 3


# =========================================================
# 📌 Q15: Find Smallest Number
# =========================================================

a, b, c = 7, 2, 9

if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)

# Output:
# 2


# =========================================================
# 📌 Q16: Check Uppercase or Lowercase
# =========================================================

ch = 'g'

if ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")

# Output:
# Lowercase


# =========================================================
# 📌 Q17: Check Triangle Validity
# =========================================================

a, b, c = 3, 4, 5

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid")

# Output:
# Valid Triangle


# =========================================================
# 📌 Q18: Check Number Range
# =========================================================

num = 15

if 10 <= num <= 20:
    print("In range")
else:
    print("Out of range")

# Output:
# In range


# =========================================================
# 📌 Q19: Electricity Bill (Simple)
# =========================================================

units = 120

if units <= 100:
    bill = units * 5
else:
    bill = units * 10

print("Bill:", bill)

# Output:
# Bill: 1200


# =========================================================
# 📌 Q20: Ternary Operator
# =========================================================

x = 10
y = 20

result = "X bigger" if x > y else "Y bigger"
print(result)

# Output:
# Y bigger


# =========================================================
# 🎯 END OF PRACTICE SET
# =========================================================