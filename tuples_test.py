# 1. Create and Print a Tuple/
# a = (3,3,2)
# print(a)
# print(type(a))
from operator import indexOf

# 2. Find Length of Tuple
# a = (2,3,4,5)
# print(len(a))


# 3. Access First and Last Element
# a = (8,7,8,9)
# print(a[0])
# print(a[-1])


# 4. Count Occurrences of an Element
# a = (8,9,9,8,9,0)
# print(a.count(9))


# 5. Find Index of an Element
# a = (4,4,3,5,5,6,6,7)
# print(a.index(5))


# 6. Traverse a Tuple
# a = (3,5,6,7)
# for num in a:
#     print(num)


# 7. Find Maximum and Minimum Element
# a = (3,4,6,8)
# print("Maximum:", max(a))
# print("Minimum:", min(a))


# 8. Find Sum and Average
# a = (8,8,8)
# total = sum(a)
# average = total / len(a)
# print(total)
# print(average)


# 9. Convert Tuple to List
# a = (2,3,5)
# b = list(a)
# print(b)


# 11. Find Largest Element Without max()/
# a = (5,5,99)
# max = 0
# for num in a:
#     if num > max:
#         max = num
# print(max)

# 12. Check Element Exists in Tuple
# a = (2,3,4)
# num = int(input("Find number in a tuple: "))
# if num in a:
#     print(f"Found {num} at position {a.index(num)}")
#     print(a)
# else:
#     print("Not found")



# 13. Count Even and Odd Numbers
# a = (4,5,6,7,8)
# odd_count = 0
# even_count = 0
# for item in a:
#     if item % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(odd_count)
# print(even_count)


# 14. Reverse a Tuple
# a =(4,4,5,9,0)
# print(a[::-1])


# 15. Tuple Unpacking
# student = ("Rahul", 21, "Python")
# name, age, course = student
# print(name)
# print(age)
# print(course)

# 16. Find Second Largest Element
# a = (4, 5, 6, 6, 9, 7, 7)
# firstlargest = float('-inf')
# secondlargest = float('-inf')
# for num in a:
#     if num > firstlargest:
#         secondlargest = firstlargest
#         firstlargest = num
#
#     elif num > secondlargest and num != firstlargest:
#         secondlargest = num
#
# print("Largest:", firstlargest)
# print("Second Largest:", secondlargest)




# 17. Find Duplicate Elements

# numbers = (1, 2, 2, 3, 4, 4, 5)
# duplicates = []
# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)
# print(duplicates)



# 18. Merge Two Tuples
#
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
#
# result = t1 + t2
#
# print(result)



# 19. Find Frequency of Each Element

# numbers = (1, 2, 1, 3, 2, 1)
# freq = {}
# for num in numbers:
#     freq[num] = freq.get(num, 0) + 1
# print(freq)


# 20. Nested Tuple Traversal
#
# students = (
#     ("Rahul", 21),
#     ("Aman", 22),
#     ("Priya", 20)
# )
#
# for name, age in students:
#     print(name, age)