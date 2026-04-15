# 1. Create a tuple with 5 numbers
t = (1, 2, 3, 4, 5)
# Output: (1, 2, 3, 4, 5)

# 2. Print the first element
print(t[0])
# Output: 1

# 3. Print the last element
print(t[-1])
# Output: 5

# 4. Slice first 3 elements
print(t[:3])
# Output: (1, 2, 3)

# 5. Check length of tuple
print(len(t))
# Output: 5

# 6. Create tuple with mixed data types
t2 = (1, "hello", 3.5, True)
# Output: (1, "hello", 3.5, True)

# 7. Access element "hello"
print(t2[1])
# Output: hello

# 8. Create single element tuple
t3 = (10,)
# Note: comma is important

# 9. Convert list to tuple
lst = [1, 2, 3]
t4 = tuple(lst)
# Output: (1, 2, 3)

# 10. Convert tuple to list
lst2 = list(t4)
# Output: [1, 2, 3]

# 11. Concatenate two tuples
t5 = (1, 2) + (3, 4)
# Output: (1, 2, 3, 4)

# 12. Repeat tuple
t6 = (1, 2) * 2
# Output: (1, 2, 1, 2)

# 13. Check if element exists
print(3 in t)
# Output: True

# 14. Find index of element
print(t.index(3))
# Output: 2

# 15. Count occurrences
t7 = (1, 2, 2, 3)
print(t7.count(2))
# Output: 2

# 16. Nested tuple
t8 = (1, (2, 3), 4)
print(t8[1][0])
# Output: 2

# 17. Tuple unpacking
a, b, c = (10, 20, 30)
print(a, b, c)
# Output: 10 20 30

# 18. Swap values using tuple
a, b = 5, 10
a, b = b, a
# Output: a=10, b=5

# 19. Loop through tuple
for i in t:
    print(i)
# Output: 1 2 3 4 5

# 20. Loop using index
for i in range(len(t)):
    print(t[i])

# 21. Sum of elements
print(sum(t))
# Output: 15

# 22. Max element
print(max(t))
# Output: 5

# 23. Min element
print(min(t))
# Output: 1

# 24. Sort tuple (convert to list)
print(sorted(t, reverse=True))
# Output: [5,4,3,2,1]

# 25. Delete tuple
del t
# Tuple deleted

# 26. Create tuple from string
t9 = tuple("hello")
# Output: ('h','e','l','l','o')

# 27. Join two tuples
t10 = (*t4, *t7)
# Output: (1,2,3,1,2,2,3)

# 28. Count total elements > 2
count = sum(1 for i in t7 if i > 2)
print(count)
# Output: 1

# 29. Reverse tuple
print(t7[::-1])
# Output: (3,2,2,1)

# 30. Find even numbers
evens = tuple(i for i in t if i % 2 == 0)
print(evens)
# Output: (2,4)

# 31. Find odd numbers
odds = tuple(i for i in t if i % 2 != 0)
print(odds)
# Output: (1,3,5)

# 32. Multiply all elements
res = 1
for i in t:
    res *= i
print(res)
# Output: 120

# 33. Check if tuple is empty
t_empty = ()
print(len(t_empty) == 0)
# Output: True

# 34. Access nested tuple
t11 = ((1,2),(3,4))
print(t11[1][1])
# Output: 4

# 35. Flatten nested tuple
flat = tuple(i for sub in t11 for i in sub)
print(flat)
# Output: (1,2,3,4)

# 36. Create tuple of squares
sq = tuple(i*i for i in range(5))
print(sq)
# Output: (0,1,4,9,16)

# 37. Tuple with range
t12 = tuple(range(1,6))
# Output: (1,2,3,4,5)

# 38. Check all elements positive
print(all(i > 0 for i in t12))
# Output: True

# 39. Check any element > 4
print(any(i > 4 for i in t12))
# Output: True

# 40. Zip two tuples
t13 = (1,2,3)
t14 = ('a','b','c')
print(tuple(zip(t13, t14)))
# Output: ((1,'a'),(2,'b'),(3,'c'))

# 41. Unzip tuple
pairs = ((1,'a'),(2,'b'))
nums, chars = zip(*pairs)
print(nums, chars)
# Output: (1,2) ('a','b')

# 42. Find common elements
t15 = (1,2,3)
t16 = (2,3,4)
common = tuple(set(t15) & set(t16))
print(common)
# Output: (2,3)

# 43. Remove duplicates
t17 = (1,2,2,3)
unique = tuple(set(t17))
print(unique)
# Output: (1,2,3)

# 44. Check equality
print((1,2,3) == (1,2,3))
# Output: True

# 45. Compare tuples
print((1,2) < (1,3))
# Output: True

# 46. Tuple inside list
lst3 = [(1,2),(3,4)]
print(lst3[0])
# Output: (1,2)

# 47. List inside tuple
t18 = ([1,2],[3,4])
t18[0].append(5)
print(t18)
# Output: ([1,2,5],[3,4])

# 48. Create dictionary from tuples
pairs = (("a",1),("b",2))
d = dict(pairs)
print(d)
# Output: {'a':1,'b':2}

# 49. Find index of max value
print(t.index(max(t)))
# Output: 4

# 50. Check if tuple is palindrome
t19 = (1,2,3,2,1)
print(t19 == t19[::-1])
# Output: True