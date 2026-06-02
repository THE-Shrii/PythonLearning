# Create a function that prints "Hello World".

# def greet():
#     print("Hello" )
#
# greet()


# Create a function that prints a person's name.

# def greet(name):
#     print("Hello, " + name + "!")
#
# greet("Shrii")


# Function to Add Two Numbers
# def add(a,b):
#     print(a+b)
#
# add(4,3)


# Function Returning a Value
# def cube(x):
#     return x**3
# cuberoot = cube(5)
# print(cuberoot)


# Check Even or Odd Using Function

# def check(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# check(int(input("Enter a number: ")))



# Find Largest of Two Numbers


# def largest(a, b):
#     if a > b:
#         return a
#     return b
#
# print(largest(15, 20))




# . Function with Default Argument

# def greet(name="User"):
#     print("Hello " + name)
# greet()
# greet("Shrii")


# Function with Keyword Arguments
# def det(name , age):
#     print(f"Your name is: {name} & you are {age} years old")
# det("Shrii",23)



# Find Factorial Using Function
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact
# print(factorial(5))




# Check Prime Number Using Function
# def prime(num):
#     if num<2:
#         return False
#     else:
#         for i in range(2,num):
#             if num % i == 0:
#                 return False
#
#         return True
# print(prime(5))





# Count Vowels in a String

# def count_vowels(text):
#     count = 0
#
#     for char in text.lower():
#         if char in "aeiou":
#             count += 1
#
#     return count
#
# print(count_vowels("Education"))



# 12. Reverse a String
# def reverse_string(text):
#     return text[::-1]
# print(reverse_string("Python"))



# Fibonacci Series Function
# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         a, b = b, a + b
#     return a
# print(fibonacci(10))


# Sum of Digits Using Function
# def sum_digits(num):
#     total = 0
#     while num > 0:
#         total += num % 10
#         num //= 10
#     return total
# print(sum_digits(1234))



# Palindrome Function

# def is_palindrome(text):
#     return text == text[::-1]
#
# print(is_palindrome("madam"))