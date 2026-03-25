# =========================================================
# 🐍 PYTHON NOTES: FUNCTIONS (DETAILED)
# =========================================================


# =========================================================
# 📌 1. WHAT IS A FUNCTION?
# =========================================================

# Function = a block of code that runs only when called

# It helps to reuse code instead of writing it again and again


# =========================================================
# 📌 2. BASIC FUNCTION
# =========================================================

def greet():
    print("Hello Shrii")

greet()

# Output:
# Hello Shrii


# =========================================================
# 📌 3. FUNCTION WITH PARAMETERS
# =========================================================

def greet(name):
    print("Hello", name)

greet("Rahul")

# Output:
# Hello Rahul


# =========================================================
# 📌 4. FUNCTION WITH RETURN VALUE
# =========================================================

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# Output:
# 8


# =========================================================
# 📌 5. DEFAULT PARAMETERS
# =========================================================

def greet(name="User"):
    print("Hello", name)

greet()
greet("Shrii")

# Output:
# Hello User
# Hello Shrii


# =========================================================
# 📌 6. KEYWORD ARGUMENTS
# =========================================================

def info(name, age):
    print(name, age)

info(age=20, name="Aman")

# Output:
# Aman 20


# =========================================================
# 📌 7. ARBITRARY ARGUMENTS (*args)
# =========================================================

def total(*numbers):
    print(sum(numbers))

total(1, 2, 3, 4)

# Output:
# 10


# =========================================================
# 📌 8. KEYWORD ARBITRARY (**kwargs)
# =========================================================

def details(**data):
    print(data)

details(name="Shrii", age=18)

# Output:
# {'name': 'Shrii', 'age': 18}


# =========================================================
# 📌 9. RECURSION (IMPORTANT)
# =========================================================

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Output:
# 120


# =========================================================
# 📌 10. LAMBDA FUNCTION
# =========================================================

add = lambda a, b: a + b
print(add(2, 3))

# Output:
# 5


# =========================================================
# 🎯 END OF NOTES
# =========================================================