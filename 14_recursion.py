# =========================================================
# 🐍 PYTHON NOTES: RECURSION (DETAILED)
# =========================================================


# =========================================================
# 📌 1. WHAT IS RECURSION?
# =========================================================

# Recursion = a function calling itself

# It repeats the same task with smaller input


# =========================================================
# 📌 2. BASIC STRUCTURE
# =========================================================

def func(n):
    if n == 0:          # Base Case (stopping condition)
        return
    print(n)
    func(n-1)           # Recursive Call

func(5)

# Output:
# 5
# 4
# 3
# 2
# 1


# =========================================================
# 📌 3. IMPORTANT CONCEPTS
# =========================================================

# 1. Base Case → stops recursion
# 2. Recursive Case → function calling itself


# =========================================================
# 📌 4. FACTORIAL USING RECURSION
# =========================================================

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Output:
# 120


# =========================================================
# 📌 5. SUM OF N NUMBERS
# =========================================================

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)

print(sum_n(5))

# Output:
# 15


# =========================================================
# 📌 6. FIBONACCI USING RECURSION
# =========================================================

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))

# Output:
# 8


# =========================================================
# 📌 7. RECURSION TRACE (IMPORTANT)
# =========================================================

# factorial(3)
# = 3 * factorial(2)
# = 3 * (2 * factorial(1))
# = 3 * (2 * 1)
# = 6


# =========================================================
# 📌 8. WRONG RECURSION (ERROR)
# =========================================================

# def wrong(n):
#     return n * wrong(n-1)   ❌ No base case → infinite recursion

# Leads to: RecursionError


# =========================================================
# 📌 9. REAL USE CASES
# =========================================================

# ✔ Factorial
# ✔ Fibonacci
# ✔ Tree/Graph problems
# ✔ Backtracking


# =========================================================
# 🎯 END OF NOTES
# =========================================================