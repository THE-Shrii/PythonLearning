# 1. Create a set with 5 elements
s = {1, 2, 3, 4, 5}
# Output: {1, 2, 3, 4, 5}

# 2. Print the set
print(s)
# Output: {1, 2, 3, 4, 5}

# 3. Check length of set
print(len(s))
# Output: 5

# 4. Add an element
s.add(6)
# Output: {1,2,3,4,5,6}

# 5. Remove an element
s.remove(3)
# Output: {1,2,4,5,6}

# 6. Discard element (no error if not found)
s.discard(10)
# No error

# 7. Pop an element
s.pop()
# Removes random element

# 8. Clear set
s2 = {1,2,3}
s2.clear()
# Output: set()

# 9. Create empty set
s3 = set()
# Note: {} creates dict

# 10. Create set from list
lst = [1,2,2,3]
s4 = set(lst)
# Output: {1,2,3}

# 11. Create set from string
s5 = set("hello")
# Output: {'h','e','l','o'}

# 12. Check membership
print(2 in s4)
# Output: True

# 13. Union of sets
a = {1,2,3}
b = {3,4,5}
print(a | b)
# Output: {1,2,3,4,5}

# 14. Intersection
print(a & b)
# Output: {3}

# 15. Difference
print(a - b)
# Output: {1,2}

# 16. Symmetric difference
print(a ^ b)
# Output: {1,2,4,5}

# 17. Using union() method
print(a.union(b))

# 18. Using intersection()
print(a.intersection(b))

# 19. Using difference()
print(a.difference(b))

# 20. Check subset
print({1,2}.issubset(a))
# Output: True

# 21. Check superset
print(a.issuperset({1,2}))
# Output: True

# 22. Check disjoint
print(a.isdisjoint({7,8}))
# Output: True

# 23. Copy set
c = a.copy()

# 24. Update set
a.update({6,7})
# Output: {1,2,3,6,7}

# 25. Remove duplicates from list
lst2 = [1,1,2,3]
print(set(lst2))
# Output: {1,2,3}

# 26. Iterate set
for i in a:
    print(i)

# 27. Set comprehension
sq = {i*i for i in range(5)}
# Output: {0,1,4,9,16}

# 28. Find max value
print(max(a))

# 29. Find min value
print(min(a))

# 30. Sum of elements
print(sum(a))

# 31. Length after adding duplicates
s6 = {1,2,2,3}
print(len(s6))
# Output: 3

# 32. Remove using pop repeatedly
while s6:
    s6.pop()

# 33. Convert set to list
lst3 = list(a)

# 34. Convert set to tuple
t = tuple(a)

# 35. Find common elements
x = {1,2,3}
y = {2,3,4}
print(x & y)
# Output: {2,3}

# 36. Find unique elements
print(x ^ y)
# Output: {1,4}

# 37. Check equality
print({1,2} == {2,1})
# Output: True

# 38. Frozen set
fs = frozenset([1,2,3])
# Immutable set

# 39. Add multiple elements
s7 = {1}
s7.update([2,3,4])

# 40. Remove element safely
s7.discard(10)
# No error

# 41. Check if set is empty
print(len(s7) == 0)

# 42. Filter even numbers
evens = {i for i in range(10) if i%2==0}
print(evens)
# Output: {0,2,4,6,8}

# 43. Filter odd numbers
odds = {i for i in range(10) if i%2!=0}

# 44. Intersection using method
print(x.intersection(y))

# 45. Difference using method
print(x.difference(y))

# 46. Symmetric difference method
print(x.symmetric_difference(y))

# 47. Check element exists
print(5 in x)

# 48. Remove element using remove()
# x.remove(10) -> ERROR if not present

# 49. Create set of characters from word
word = "python"
print(set(word))
# Output: {'p','y','t','h','o','n'}

# 50. Count unique elements in list
lst4 = [1,2,2,3,4,4]
print(len(set(lst4)))
# Output: 4