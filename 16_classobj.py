# =========================================================
# 🐍 PYTHON OOP COMPLETE BASICS
# Class, Object, Instance, self, Constructor, Static Method
# =========================================================


# =========================================================
# 📌 1. CLASS & OBJECT
# =========================================================

class Student:
    name = "Default"

# Object creation
s1 = Student()
print(s1.name)

# Output:
# Default


# =========================================================
# 📌 2. INSTANCE & INSTANCE VARIABLES
# =========================================================

class Student:
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age

s1 = Student("Shrii", 20)
s2 = Student("Rahul", 22)

print(s1.name, s1.age)
print(s2.name, s2.age)

# Output:
# Shrii 20
# Rahul 22


# =========================================================
# 📌 3. SELF PARAMETER
# =========================================================

class Demo:
    def show(self):
        print("This is self:", self)

d = Demo()
d.show()

# Output:
# This is self: <__main__.Demo object at ...>


# =========================================================
# 📌 4. METHODS
# =========================================================

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s = Student("Shrii")
s.greet()

# Output:
# Hello Shrii


# =========================================================
# 📌 5. CONSTRUCTOR (__init__)
# =========================================================

class Car:
    def __init__(self, brand):
        self.brand = brand

c = Car("BMW")
print(c.brand)

# Output:
# BMW


# =========================================================
# 📌 6. DEFAULT CONSTRUCTOR
# =========================================================

class Test:
    def __init__(self):
        print("Constructor called")

t = Test()

# Output:
# Constructor called


# =========================================================
# 📌 7. STATIC METHOD
# =========================================================

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 4))

# Output:
# 7


# =========================================================
# 📌 8. CLASS vs INSTANCE VARIABLE
# =========================================================

class Demo:
    x = 10   # class variable

    def __init__(self):
        self.y = 20   # instance variable

d1 = Demo()
d2 = Demo()

print(d1.x, d1.y)
print(d2.x, d2.y)

# Output:
# 10 20
# 10 20


# =========================================================
# 📌 9. MODIFY VARIABLES
# =========================================================

d1.x = 100
Demo.x = 50

print(d1.x, d2.x)

# Output:
# 100 50


# =========================================================
# 🎯 END OF OOP BASICS
# =========================================================