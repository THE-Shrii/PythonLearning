# =========================================================
# 🐍 PYTHON LISTS
# =========================================================


# ---------------------------------------------------------
# 📌 1. DEFINITION
# ---------------------------------------------------------
# List is a collection of elements stored in a single variable
# It is:
# ✔ Ordered === A list is called ordered because the elements are stored in a fixed sequence, and Python remembers that order.
# ✔ Mutable (can be changed)
# ✔ Allows duplicate values


# ---------------------------------------------------------
# 📌 2. CREATING LIST
# ---------------------------------------------------------
lst = [1, 2, 3, "Python", 3.5]
print(lst)

# Output: [1, 2, 3, 'Python', 3.5]


# ---------------------------------------------------------
# 📌 3. INDEXING
# ---------------------------------------------------------
# Index starts from 0

lst = [10, 20, 30, 40]

print(lst[0])   # first element
print(lst[-1])  # last element

# Output:
# 10
# 40


# ---------------------------------------------------------
# 📌 4. SLICING
# ---------------------------------------------------------
# Syntax: list[start:end:step]

lst = [10, 20, 30, 40, 50]

print(lst[1:4])
print(lst[::-1])

# Output:
# [20, 30, 40]
# [50, 40, 30, 20, 10]


# ---------------------------------------------------------
# 📌 5. MODIFY LIST (MUTABLE)
# ---------------------------------------------------------
lst = [1, 2, 3]
lst[0] = 100
print(lst)

# Output: [100, 2, 3]


# ---------------------------------------------------------
# 📌 6. LIST METHODS (VERY IMPORTANT)
# ---------------------------------------------------------

# append() → add element at end
lst = [1, 2, 3]
lst.append(4)
print(lst)
# Output: [1, 2, 3, 4]


# extend() → add multiple elements
lst = [1, 2]
lst.extend([3, 4])
print(lst)
# Output: [1, 2, 3, 4]


# insert() → insert at specific position
lst = [1, 2, 3]
lst.insert(1, 100)
print(lst)
# Output: [1, 100, 2, 3]


# remove() → remove element by value
lst = [1, 2, 3]
lst.remove(2)
print(lst)
# Output: [1, 3]


# pop() → remove element by index
lst = [1, 2, 3]
lst.pop()
print(lst)
# Output: [1, 2]


# clear() → remove all elements
lst = [1, 2, 3]
lst.clear()
print(lst)
# Output: []


# index() → find position
lst = [10, 20, 30]
print(lst.index(20))
# Output: 1


# count() → count occurrences
lst = [1, 2, 2, 3]
print(lst.count(2))
# Output: 2


# sort() → sort list
lst = [3, 1, 2]
lst.sort()
print(lst)
# Output: [1, 2, 3]


# reverse() → reverse list
lst = [1, 2, 3]
lst.reverse()
print(lst)
# Output: [3, 2, 1]


# copy() → copy list
lst = [1, 2, 3]
new_lst = lst.copy()
print(new_lst)
# Output: [1, 2, 3]


# ---------------------------------------------------------
# 📌 7. OPERATORS ON LIST
# ---------------------------------------------------------

# Concatenation
a = [1, 2]
b = [3, 4]
print(a + b)
# Output: [1, 2, 3, 4]

# Repetition
print([1, 2] * 2)
# Output: [1, 2, 1, 2]

# Membership
lst = [1, 2, 3]
print(2 in lst)
print(5 not in lst)
# Output:
# True
# True


# ---------------------------------------------------------
# 📌 8. LOOP THROUGH LIST
# ---------------------------------------------------------
lst = [10, 20, 30]

for i in lst:
    print(i)

# Output:
# 10
# 20
# 30


# ---------------------------------------------------------
# 📌 9. LENGTH OF LIST
# ---------------------------------------------------------
lst = [1, 2, 3, 4]
print(len(lst))
# Output: 4


# ---------------------------------------------------------
# 📌 10. NESTED LIST
# ---------------------------------------------------------
lst = [1, [2, 3], [4, 5]]
print(lst[1])
print(lst[1][0])

# Output:
# [2, 3]
# 2


# ---------------------------------------------------------
# 📌 11. LIST COMPREHENSION
# ---------------------------------------------------------
# Short way to create list

lst = [x**2 for x in range(5)]
print(lst)

# Output: [0, 1, 4, 9, 16]


# ---------------------------------------------------------
# 📌 12. PRACTICE EXAMPLES
# ---------------------------------------------------------

# Find max element
lst = [10, 50, 20]
print(max(lst))
# Output: 50

# Find min element
print(min(lst))
# Output: 10

# Sum of list
print(sum(lst))
# Output: 80


# =========================================================
# 🎯 END OF LIST NOTES
# =========================================================