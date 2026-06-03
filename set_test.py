# 1. Create and Print a Set
# a  = {1,2,3}
# print(a)
# print(type(a))

# 2. Remove Duplicate Elements from a List
# a = [1, 2, 2, 3, 4, 4, 5]
# unique = set(a)
# print(unique)

# 3. Check if Element Exists
# fruits = {"Apple", "Banana", "Mango"}
# if "Apple" in fruits:
#     print("Apple is in fruits")
# else:
#     print("Apple is not in fruits")


# 4. Add an Element
# numbers = {1, 2, 3}
# numbers.add(4)
# print(numbers)

# 5. Remove an Element
# a = {1,2,3}
# a.remove(2)
# print(a)


# 6. Find Union of Two Sets
# a = {2,3,4}
# b = {4,5}
# print(a.union(b))

# 7. Find Intersection
# a = {2,3,4}
# b = {4,5}
# print(a.intersection(b))


# 8. Find Difference
# a = {2,3,4}
# b = {4,5}
# print(a-b)
# print(b-a)


# 9. Find Symmetric Difference
# a = {3,3,5,6,7}
# b = {4,5,9}
# print(a.symmetric_difference(b))


# 10. Traverse a Set
# a = {3,3,5,6,7}
# for  num in a:
#     print(num)



# 11. Count Unique Elements
# a = {1,23,323,23,4,5,55,5,8,}
# unique_count = len(set(a))
# print(unique_count)



# 12. Check Subset
# a = {3,4}
# b = {3,4,5,6}
# print(a.issubset(b))


# 13. Check Superset
# a = {3,4,5,6,7}
# b = {3,4,5,6}
# print(a.issuperset(b))



# 14. Find Common Elements in Lists Using Set
# a = [3,3,45,6,7]
# b = [2,3,4,5]
# com = set(a) & set(b)
# print(com)


# 15. Remove Multiple Duplicates from String
# a = "Pythonn"
# unique_char = set(a)
# print(unique_char)



# 16. Find Missing Elements Between Two Sets
# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 4}
# missing = set1 - set2
# print(missing)


# 17. Check Two Sets Are Equal
# a = {1,2}
# b = {1,2}
# print(a == b)



# 18. Find Unique Words in Sentence/
# sentence = "python java python c java"
# words = sentence.split()
# unique_words = set(words)
# print(unique_words)



# 19. Find Duplicates Using Set
#
# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# seen = set()
# duplicates = set()
# for num in numbers:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)
# print(duplicates)



# 20. Find Unique Characters Between Two Strings

# str1 = "abcde"
# str2 = "cdefg"
# result = set(str1) ^ set(str2)
# print(result)