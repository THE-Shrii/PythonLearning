# =========================================================
# 🐍 PYTHON STRINGS 
# =========================================================


# ---------------------------------------------------------
# 📌 1. DEFINITION
# ---------------------------------------------------------
# String is a sequence of characters enclosed in quotes
# It is IMMUTABLE (cannot be changed after creation)


# ---------------------------------------------------------
# 📌 2. CREATING STRINGS
# ---------------------------------------------------------

str1 = "Hello"
str2 = 'Python'
str3 = """This is
multi-line string"""

print(str1, str2)
# Output: Hello Python


# ---------------------------------------------------------
# 📌 3. STRING INDEXING
# ---------------------------------------------------------
# Index starts from 0

text = "Python"

print(text[0])   # First character
print(text[3])   # Character at index 3
print(text[-1])  # Last character

# Output:
# P
# h
# n


# ---------------------------------------------------------
# 📌 4. STRING SLICING
# ---------------------------------------------------------
# Syntax: string[start:end:step]

text = "Python"

print(text[0:3])   # from index 0 to 2
print(text[2:])    # from index 2 to end
print(text[:4])    # from start to index 3
print(text[::-1])  # reverse string

# Output:
# Pyt
# thon
# Pyth
# nohtyP


# ---------------------------------------------------------
# 📌 5. STRING CONCATENATION
# ---------------------------------------------------------

a = "Hello"
b = "World"

print(a + " " + b)
# Output: Hello World


# ---------------------------------------------------------
# 📌 6. STRING REPETITION
# ---------------------------------------------------------

print("Hi " * 3)
# Output: Hi Hi Hi


# ---------------------------------------------------------
# 📌 7. STRING METHODS (VERY IMPORTANT)
# ---------------------------------------------------------

text = "python programming"

print(text.upper())      # uppercase
print(text.lower())      # lowercase
print(text.title())      # title case
print(text.capitalize()) # first letter capital

# Output:
# PYTHON PROGRAMMING
# python programming
# Python Programming
# Python programming


# ---------------------------------------------------------
# 📌 8. SEARCHING IN STRING
# ---------------------------------------------------------

text = "Python Programming"

print(text.find("Pro"))   # returns index
print(text.count("m"))    # count occurrences

# Output:
# 7
# 2


# ---------------------------------------------------------
# 📌 9. REPLACE IN STRING
# ---------------------------------------------------------

text = "Hello World"
print(text.replace("World", "Python"))

# Output: Hello Python


# ---------------------------------------------------------
# 📌 10. SPLIT & JOIN
# ---------------------------------------------------------

text = "apple banana mango"

words = text.split()
print(words)

joined = "-".join(words)
print(joined)

# Output:
# ['apple', 'banana', 'mango']
# apple-banana-mango


# ---------------------------------------------------------
# 📌 11. CHECK FUNCTIONS
# ---------------------------------------------------------

text = "Python123"

print(text.isalpha())   # only letters
print(text.isdigit())   # only numbers
print(text.isalnum())   # letters + numbers

# Output:
# False
# False
# True


# ---------------------------------------------------------
# 📌 12. STRING FORMATTING
# ---------------------------------------------------------

name = "Shrii"
age = 20

print(f"My name is {name} and I am {age} years old")

# Output:
# My name is Shrii and I am 20 years old


# ---------------------------------------------------------
# 📌 13. ESCAPE CHARACTERS
# ---------------------------------------------------------

print("Hello\nWorld")   # new line
print("Hello\tWorld")   # tab space

# Output:
# Hello
# World
# Hello    World


# ---------------------------------------------------------
# 📌 14. IMMUTABILITY
# ---------------------------------------------------------

text = "Python"

# text[0] = 'J' ❌ Not allowed

# To modify:
text = "J" + text[1:]
print(text)

# Output: Jython


# ---------------------------------------------------------
# 📌 15. MEMBERSHIP OPERATOR
# ---------------------------------------------------------

text = "Python"

print("Py" in text)
print("Java" not in text)

# Output:
# True
# True


# ---------------------------------------------------------
# 📌 16. LENGTH OF STRING
# ---------------------------------------------------------

text = "Python"
print(len(text))

# Output: 6


# ---------------------------------------------------------
# 📌 17. PRACTICE EXAMPLES
# ---------------------------------------------------------

# Reverse string
s = "hello"
print(s[::-1])
# Output: olleh

# Count vowels
s = "python"
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Vowels:", count)
# Output: Vowels: 1





# ---------------------------------------------------------
# 📌 1. upper() → Convert to uppercase
# ---------------------------------------------------------
text = "python"
print(text.upper())

# Output: PYTHON


# ---------------------------------------------------------
# 📌 2. lower() → Convert to lowercase
# ---------------------------------------------------------
text = "PYTHON"
print(text.lower())

# Output: python


# ---------------------------------------------------------
# 📌 3. title() → First letter of each word capital
# ---------------------------------------------------------
text = "python programming"
print(text.title())

# Output: Python Programming


# ---------------------------------------------------------
# 📌 4. capitalize() → First letter capital only
# ---------------------------------------------------------
text = "python programming"
print(text.capitalize())

# Output: Python programming


# ---------------------------------------------------------
# 📌 5. strip() → Remove spaces from both sides
# ---------------------------------------------------------
text = "   hello   "
print(text.strip())

# Output: hello


# ---------------------------------------------------------
# 📌 6. lstrip() → Remove left spaces
# ---------------------------------------------------------
text = "   hello"
print(text.lstrip())

# Output: hello


# ---------------------------------------------------------
# 📌 7. rstrip() → Remove right spaces
# ---------------------------------------------------------
text = "hello   "
print(text.rstrip())

# Output: hello


# ---------------------------------------------------------
# 📌 8. find() → Find position of substring
# ---------------------------------------------------------
text = "python programming"
print(text.find("pro"))

# Output: 7


# ---------------------------------------------------------
# 📌 9. count() → Count occurrences
# ---------------------------------------------------------
text = "banana"
print(text.count("a"))

# Output: 3


# ---------------------------------------------------------
# 📌 10. replace() → Replace substring
# ---------------------------------------------------------
text = "hello world"
print(text.replace("world", "python"))

# Output: hello python


# ---------------------------------------------------------
# 📌 11. split() → Convert string to list
# ---------------------------------------------------------
text = "apple banana mango"
print(text.split())

# Output: ['apple', 'banana', 'mango']


# ---------------------------------------------------------
# 📌 12. join() → Join list into string
# ---------------------------------------------------------
words = ['apple', 'banana', 'mango']
print("-".join(words))

# Output: apple-banana-mango


# ---------------------------------------------------------
# 📌 13. startswith() → Check starting
# ---------------------------------------------------------
text = "python"
print(text.startswith("py"))

# Output: True


# ---------------------------------------------------------
# 📌 14. endswith() → Check ending
# ---------------------------------------------------------
text = "python"
print(text.endswith("on"))

# Output: True


# ---------------------------------------------------------
# 📌 15. isalpha() → Only letters?
# ---------------------------------------------------------
text = "python"
print(text.isalpha())

# Output: True


# ---------------------------------------------------------
# 📌 16. isdigit() → Only numbers?
# ---------------------------------------------------------
text = "12345"
print(text.isdigit())

# Output: True


# ---------------------------------------------------------
# 📌 17. isalnum() → Letters + numbers?
# ---------------------------------------------------------
text = "python123"
print(text.isalnum())

# Output: True


# ---------------------------------------------------------
# 📌 18. len() → Length of string
# ---------------------------------------------------------
text = "python"
print(len(text))

# Output: 6


# ---------------------------------------------------------
# 📌 19. format() / f-string → Formatting
# ---------------------------------------------------------
name = "Shrii"
age = 20

print(f"My name is {name} and I am {age} years old")

# Output: My name is Shrii and I am 20 years old


# ---------------------------------------------------------
# 📌 20. swapcase() → Upper ↔ Lower
# ---------------------------------------------------------
text = "PyThOn"
print(text.swapcase())

# Output: pYtHoN

# =========================================================
# 🎯 END OF STRING NOTES
# =========================================================