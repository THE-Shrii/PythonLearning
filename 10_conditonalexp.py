# =========================================================
# 🐍 PYTHON NOTES: CONDITIONAL EXPRESSIONS (if-else)
# =========================================================


# =========================================================
# 📌 1. DEFINITION
# =========================================================

# Conditional Statements:
# These are used to make decisions in a program.

# They execute different blocks of code based on conditions.

# Example:
age = 18

if age >= 18:
    print("You can vote")

# Output:
# You can vote


# =========================================================
# 📌 2. TYPES OF CONDITIONAL STATEMENTS
# =========================================================

# 1. if
# 2. if-else
# 3. if-elif-else
# 4. Nested if


# =========================================================
# 📌 3. IF STATEMENT
# =========================================================

x = 10

if x > 5:
    print("x is greater than 5")

# Output:
# x is greater than 5


# =========================================================
# 📌 4. IF-ELSE STATEMENT
# =========================================================

x = 3

if x > 5:
    print("Greater")
else:
    print("Smaller")

# Output:
# Smaller


# =========================================================
# 📌 5. IF-ELIF-ELSE
# =========================================================

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

# Output:
# Grade B


# =========================================================
# 📌 6. NESTED IF
# =========================================================

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")

# Output:
# Eligible to vote


# =========================================================
# 📌 7. CONDITIONAL (TERNARY) EXPRESSION
# =========================================================

# Short form of if-else

a = 10
b = 20

result = "a is greater" if a > b else "b is greater"
print(result)

# Output:
# b is greater


# =========================================================
# 📌 8. MULTIPLE CONDITIONS (LOGICAL OPERATORS)
# =========================================================

age = 25

if age > 18 and age < 60:
    print("Working age")

# Output:
# Working age


# =========================================================
# 📌 9. INPUT WITH CONDITIONS
# =========================================================

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example Run:
# Enter number: 4
# Output:
# Even


# =========================================================
# 📌 10. IMPORTANT POINTS
# =========================================================

# ✔ Indentation is important
# ✔ Condition must be True/False
# ✔ Use comparison operators (>, <, ==)
# ✔ Use logical operators (and, or, not)


# =========================================================
# 📌 11. COMMON ERRORS
# =========================================================

# ❌ Missing colon
# if x > 5
#     print("Error")

# ❌ Wrong indentation


# =========================================================
# 📌 12. REAL-LIFE EXAMPLES
# =========================================================

# Login System
password = "1234"

if password == "1234":
    print("Login Successful")
else:
    print("Wrong Password")

# Output:
# Login Successful


# =========================================================
# 🎯 END OF NOTES
# =========================================================









# =========================================================
# 🐍 PYTHON: IF, IF-ELIF-ELSE LADDER PROGRAMS
# =========================================================


# =========================================================
# 📌 1. SIMPLE IF PROGRAM
# =========================================================

# Program: Check if number is positive

num = 5

if num > 0:
    print("Positive Number")

# Output:
# Positive Number


# =========================================================
# 📌 2. IF-ELSE PROGRAM
# =========================================================

# Program: Check Even or Odd

num = 4

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Output:
# Even


# =========================================================
# 📌 3. IF-ELIF-ELSE LADDER PROGRAM
# =========================================================

# Program: Grade System

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Output:
# Grade B


# =========================================================
# 📌 4. MULTIPLE CONDITION PROGRAM
# =========================================================

# Program: Check age category

age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Output:
# Adult


# =========================================================
# 📌 5. NESTED IF PROGRAM
# =========================================================

# Program: Voting eligibility

age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Too young")

# Output:
# Eligible to vote


# =========================================================
# 📌 6. INPUT BASED PROGRAM
# =========================================================

# Program: Check largest number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest is:", a)
elif b > c:
    print("Largest is:", b)
else:
    print("Largest is:", c)

# Example Run:
# Enter first number: 5
# Enter second number: 10
# Enter third number: 7
# Output:
# Largest is: 10


# =========================================================
# 📌 7. TERNARY (SHORT IF-ELSE)
# =========================================================

x = 10
y = 20

print("x is greater") if x > y else print("y is greater")

# Output:
# y is greater


# =========================================================
# 🎯 END OF PROGRAMS
# =========================================================