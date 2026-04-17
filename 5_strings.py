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

# =========================================================
# 🐍 PYTHON NOTES: LIST
# =========================================================


# =========================================================
# 📌 1. DEFINITION
# =========================================================

# List:
# A list is a collection of items stored in a single variable.

# It is:
# ✔ Ordered
# ✔ Mutable (changeable)
# ✔ Allows duplicate values

# Example:
lst = [1, 2, 3, 4]
print(lst)

# Output:
# [1, 2, 3, 4]


# =========================================================
# 📌 2. CREATING LIST
# =========================================================

a = [1, 2, 3]
b = ["apple", "banana"]
c = [1, "Shrii", 5.5, True]

print(a, b, c)

# Output:
# [1, 2, 3] ['apple', 'banana'] [1, 'Shrii', 5.5, True]


# =========================================================
# 📌 3. INDEXING
# =========================================================

lst = [10, 20, 30, 40]

print(lst[0])   # 10
print(lst[-1])  # 40


# =========================================================
# 📌 4. SLICING
# =========================================================

lst = [10, 20, 30, 40, 50]

print(lst[1:4])   # [20, 30, 40]
print(lst[:3])    # [10, 20, 30]
print(lst[2:])    # [30, 40, 50]


# =========================================================
# 📌 5. MUTABILITY (IMPORTANT)
# =========================================================

lst = [1, 2, 3]
lst[0] = 100

print(lst)

# Output:
# [100, 2, 3]


# =========================================================
# 📌 6. LIST METHODS
# =========================================================

lst = [1, 2, 3]

# append() → add element
lst.append(4)
print(lst)   # [1,2,3,4]

# insert() → add at index
lst.insert(1, 10)
print(lst)   # [1,10,2,3,4]

# extend() → add multiple
lst.extend([5, 6])
print(lst)   # [1,10,2,3,4,5,6]

# remove() → remove value
lst.remove(10)
print(lst)   # [1,2,3,4,5,6]

# pop() → remove last/index
lst.pop()
print(lst)   # [1,2,3,4,5]

# index() → position
print(lst.index(3))  # 2

# count() → frequency
print(lst.count(2))  # 1

# sort() → ascending
lst.sort()
print(lst)

# reverse()
lst.reverse()
print(lst)

# copy()
new_lst = lst.copy()
print(new_lst)

# clear()
lst.clear()
print(lst)


# =========================================================
# 📌 7. LIST OPERATIONS
# =========================================================

a = [1, 2]
b = [3, 4]

print(a + b)   # concatenation → [1,2,3,4]
print(a * 2)   # repetition → [1,2,1,2]


# =========================================================
# 📌 8. MEMBERSHIP
# =========================================================

lst = [1, 2, 3]

print(2 in lst)      # True
print(5 not in lst)  # True


# =========================================================
# 📌 9. LOOPING IN LIST
# =========================================================

lst = [10, 20, 30]

for i in lst:
    print(i)

# Output:
# 10
# 20
# 30


# =========================================================
# 📌 10. LIST COMPREHENSION (IMPORTANT)
# =========================================================

lst = [x*x for x in range(5)]
print(lst)

# Output:
# [0, 1, 4, 9, 16]


# =========================================================
# 📌 11. NESTED LIST
# =========================================================

lst = [[1,2], [3,4]]

print(lst[0][1])   # 2


# =========================================================
# 📌 12. LENGTH FUNCTION
# =========================================================

lst = [1,2,3]
print(len(lst))

# Output:
# 3


# =========================================================
# 📌 13. IMPORTANT CONCEPT: ORDERED
# =========================================================

# Ordered means:
# Elements maintain their position

lst = [10, 20, 30]
print(lst[1])  # always 20


# =========================================================
# 🎯 END OF NOTES
# =========================================================

# =========================================================
# 🐍 PYTHON NOTES: TUPLE
# =========================================================


# =========================================================
# 📌 1. DEFINITION
# =========================================================

# Tuple:
# A tuple is a collection of items stored in a single variable.

# It is:
# ✔ Ordered
# ✔ Immutable (cannot be changed)
# ✔ Allows duplicate values

# Example:
t = (1, 2, 3)
print(t)

# Output:
# (1, 2, 3)


# =========================================================
# 📌 2. CREATING TUPLE
# =========================================================

a = (1, 2, 3)
b = ("apple", "banana")
c = (1, "Shrii", 5.5, True)

print(a, b, c)

# Output:
# (1, 2, 3) ('apple', 'banana') (1, 'Shrii', 5.5, True)


# =========================================================
# 📌 3. SINGLE ELEMENT TUPLE (IMPORTANT)
# =========================================================

t = (5,)   # comma is required
print(type(t))

# Output:
# <class 'tuple'>


# =========================================================
# 📌 4. INDEXING
# =========================================================

t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40


# =========================================================
# 📌 5. SLICING
# =========================================================

t = (10, 20, 30, 40, 50)

print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[2:])    # (30, 40, 50)


# =========================================================
# 📌 6. IMMUTABILITY (IMPORTANT)
# =========================================================

t = (1, 2, 3)

# t[0] = 100 ❌ Error (not allowed)

print(t)

# Output:
# (1, 2, 3)


# =========================================================
# 📌 7. TUPLE METHODS
# =========================================================

t = (1, 2, 2, 3, 2)

# count() → number of occurrences
print("Count:", t.count(2))

# index() → first occurrence index
print("Index:", t.index(2))

# Output:
# Count: 3
# Index: 1


# =========================================================
# 📌 8. TUPLE OPERATIONS
# =========================================================

a = (1, 2)
b = (3, 4)

# Concatenation
print(a + b)   # (1,2,3,4)

# Repetition
print(a * 2)   # (1,2,1,2)


# =========================================================
# 📌 9. MEMBERSHIP
# =========================================================

t = (1, 2, 3)

print(2 in t)      # True
print(5 not in t)  # True


# =========================================================
# 📌 10. LOOPING
# =========================================================

t = (10, 20, 30)

for i in t:
    print(i)

# Output:
# 10
# 20
# 30


# =========================================================
# 📌 11. TUPLE PACKING & UNPACKING
# =========================================================

# Packing
t = (1, 2, 3)

# Unpacking
a, b, c = t

print(a, b, c)

# Output:
# 1 2 3


# =========================================================
# 📌 12. NESTED TUPLE
# =========================================================

t = ((1, 2), (3, 4))

print(t[0][1])   # 2


# =========================================================
# 📌 13. CONVERTING TUPLE
# =========================================================

# tuple → list
t = (1, 2, 3)
lst = list(t)
print(lst)

# list → tuple
lst = [4, 5, 6]
t = tuple(lst)
print(t)

# Output:
# [1, 2, 3]
# (4, 5, 6)


# =========================================================
# 📌 14. LENGTH FUNCTION
# =========================================================

t = (1, 2, 3)
print(len(t))

# Output:
# 3


# =========================================================
# 📌 15. IMPORTANT CONCEPT: ORDERED
# =========================================================

# Ordered means:
# Elements keep their position

t = (10, 20, 30)
print(t[1])   # always 20


# =========================================================
# 🎯 END OF NOTES
# =========================================================




# =========================================================
# 🐍 PYTHON NOTES: DICTIONARY
# =========================================================


# =========================================================
# 📌 1. DEFINITION
# =========================================================

# Dictionary:
# A dictionary is a collection of key-value pairs.

# It is:
# ✔ Ordered (Python 3.7+)
# ✔ Mutable
# ✔ Keys must be unique

# Example:
d = {"name": "Shrii", "age": 20}
print(d)

# Output:
# {'name': 'Shrii', 'age': 20}


# =========================================================
# 📌 2. CREATING DICTIONARY
# =========================================================

d1 = {"a": 1, "b": 2}
d2 = dict(x=10, y=20)

print(d1, d2)

# Output:
# {'a': 1, 'b': 2} {'x': 10, 'y': 20}


# =========================================================
# 📌 3. ACCESSING VALUES
# =========================================================

d = {"name": "Shrii", "age": 20}

print(d["name"])      # direct access
print(d.get("age"))   # safe access

# Output:
# Shrii
# 20


# =========================================================
# 📌 4. ADD / UPDATE
# =========================================================

d = {"a": 1}

d["b"] = 2      # add
d["a"] = 10     # update

print(d)

# Output:
# {'a': 10, 'b': 2}


# =========================================================
# 📌 5. REMOVE ELEMENTS
# =========================================================

d = {"a": 1, "b": 2, "c": 3}

d.pop("b")      # remove key
print(d)

d.popitem()     # remove last item
print(d)

del d["a"]      # delete key
print(d)

# Output:
# {'a': 1, 'c': 3}
# {'a': 1}
# {}


# =========================================================
# 📌 6. LOOPING IN DICTIONARY
# =========================================================

d = {"x": 1, "y": 2}

# keys
for k in d:
    print(k)

# values
for v in d.values():
    print(v)

# key-value
for k, v in d.items():
    print(k, v)

# Output:
# x y
# 1 2
# x 1
# y 2


# =========================================================
# 📌 7. IMPORTANT METHODS
# =========================================================

d = {"a": 1, "b": 2}

print(d.keys())     # keys
print(d.values())   # values
print(d.items())    # key-value pairs

# Output:
# dict_keys(['a','b'])
# dict_values([1,2])
# dict_items([('a',1),('b',2)])


# =========================================================
# 📌 8. COPY & CLEAR
# =========================================================

d = {"a": 1}

d2 = d.copy()
print(d2)

d.clear()
print(d)

# Output:
# {'a': 1}
# {}


# =========================================================
# 📌 9. UPDATE METHOD
# =========================================================

d1 = {"a": 1}
d2 = {"b": 2}

d1.update(d2)
print(d1)

# Output:
# {'a': 1, 'b': 2}


# =========================================================
# 📌 10. FROMKEYS
# =========================================================

keys = ["a", "b"]
d = dict.fromkeys(keys, 0)

print(d)

# Output:
# {'a': 0, 'b': 0}


# =========================================================
# 📌 11. NESTED DICTIONARY
# =========================================================

d = {
    "student": {
        "name": "Shrii",
        "age": 20
    }
}

print(d["student"]["name"])

# Output:
# Shrii


# =========================================================
# 📌 12. DICTIONARY COMPREHENSION
# =========================================================

d = {x: x*x for x in range(5)}
print(d)

# Output:
# {0:0,1:1,2:4,3:9,4:16}


# =========================================================
# 📌 13. LENGTH FUNCTION
# =========================================================

d = {"a":1,"b":2}
print(len(d))

# Output:
# 2


# =========================================================
# 📌 14. MEMBERSHIP
# =========================================================

d = {"a":1,"b":2}

print("a" in d)      # True
print("c" not in d)  # True


# =========================================================
# 📌 15. IMPORTANT CONCEPTS
# =========================================================

# ✔ Keys must be unique
d = {"a":1,"a":2}
print(d)

# Output:
# {'a': 2}

# ✔ Keys must be immutable (str, int, tuple)
# ❌ list cannot be key


# =========================================================
# 🎯 END OF NOTES
# =========================================================


# =========================================================
# 🐍 PYTHON NOTES: SET
# =========================================================


# =========================================================
# 📌 1. DEFINITION
# =========================================================

# Set:
# A set is a collection of unique elements.

# It is:
# ✔ Unordered
# ✔ Mutable
# ✔ Does NOT allow duplicates

# Example:
s = {1, 2, 3}
print(s)

# Output:
# {1, 2, 3}


# =========================================================
# 📌 2. DUPLICATES REMOVED
# =========================================================

s = {1, 2, 2, 3}
print(s)

# Output:
# {1, 2, 3}


# =========================================================
# 📌 3. CREATING SET
# =========================================================

a = {1, 2, 3}
b = set([4, 5, 6])

print(a, b)

# Output:
# {1, 2, 3} {4, 5, 6}


# =========================================================
# 📌 4. EMPTY SET (IMPORTANT)
# =========================================================

s = set()   # correct
print(type(s))

# {} → dictionary, not set


# =========================================================
# 📌 5. ADDING ELEMENTS
# =========================================================

s = {1, 2}

s.add(3)
print(s)

s.update([4, 5])
print(s)

# Output:
# {1,2,3}
# {1,2,3,4,5}


# =========================================================
# 📌 6. REMOVING ELEMENTS
# =========================================================

s = {1, 2, 3}

s.remove(2)   # error if not found
print(s)

s.discard(10) # no error
print(s)

s.pop()       # removes random element
print(s)

# Output:
# {1,3}
# {1,3}
# random removed


# =========================================================
# 📌 7. SET OPERATIONS (VERY IMPORTANT)
# =========================================================

a = {1, 2, 3}
b = {2, 3, 4}

# Union
print(a | b)         # {1,2,3,4}

# Intersection
print(a & b)         # {2,3}

# Difference
print(a - b)         # {1}

# Symmetric Difference
print(a ^ b)         # {1,4}


# =========================================================
# 📌 8. METHODS (IMPORTANT)
# =========================================================

a = {1, 2}
b = {2, 3}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# Output:
# {1,2,3}
# {2}
# {1}
# {1,3}


# =========================================================
# 📌 9. RELATION METHODS
# =========================================================

a = {1, 2, 3}

print({1}.issubset(a))      # True
print(a.issuperset({1}))    # True
print(a.isdisjoint({10}))   # True


# =========================================================
# 📌 10. LOOPING
# =========================================================

s = {1, 2, 3}

for i in s:
    print(i)

# Output:
# 1 2 3 (order may vary)


# =========================================================
# 📌 11. SET COMPREHENSION
# =========================================================

s = {x*x for x in range(5)}
print(s)

# Output:
# {0,1,4,9,16}


# =========================================================
# 📌 12. LENGTH FUNCTION
# =========================================================

s = {1, 2, 3}
print(len(s))

# Output:
# 3


# =========================================================
# 📌 13. MEMBERSHIP
# =========================================================

s = {1, 2, 3}

print(2 in s)      # True
print(5 not in s)  # True


# =========================================================
# 📌 14. CONVERSION
# =========================================================

lst = [1, 2, 2, 3]

print(set(lst))       # remove duplicates
print(list(set(lst))) # back to list

# Output:
# {1,2,3}
# [1,2,3]


# =========================================================
# 📌 15. IMPORTANT CONCEPTS
# =========================================================

# ✔ Unordered → no indexing
# s[0] ❌ not allowed

# ✔ Only immutable elements allowed
# {1, [2,3]} ❌ error


# =========================================================
# 🎯 END OF NOTES
# =========================================================