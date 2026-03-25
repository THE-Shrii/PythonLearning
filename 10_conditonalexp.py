
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


