# 1. Create and Print a Dictionary
# a = {
#     'name':"shrii",
#     'age':20,
# }
# print(a)
# print(a['name'])
# print(a['age'])
# print(type(a))


# 2. Access Value Using Key
# b = {
#     'name':"shrii",
#     'age':20,
# }
# print(b['name'])
# print(b['age'])


# 3. Add a New Key-Value Pair
# c = {
#     'a':1,
#     'b':2,
#     'c':3,
#     'd':4,
# }
# c['e'] = 5
# print(c)


# 4. Update a Value
# d = {
#     "a":"apple"
# }
# d["a"] = "America"
# print(d)


# 5. Delete a Key
# e = {
#     "country":"USA",
#     "state":"CA",
#     "city":"New York"
# }
# del e["city"]
# print(e)



# 6. Traverse Keys and Values
# student = {
#     "name": "Rahul",
#     "age": 21,
#     "city": "Delhi"
# }
#
# for key, value in student.items():
#     print(key, ":", value)



# 7. Sum All Values
#
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }
#
# print(sum(data.values()))

# 8. Find Maximum Value
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }
# print(max(data.values()))

# 9. Find Key with Maximum Value
# marks = {
#     "Math": 80,
#     "Science": 95,
#     "English": 70
# }
#
# max_key = max(marks, key=marks.get)
#
# print(max_key)


# 10. Check if Key Exists
# student = {
#     "name": "Neha",
#     "age": 21
# }
#
# if "name" in student:
#     print("Key Found")
# else:
#     print("Key Not Found")


# 11. Count Frequency of Elements
# numbers = [1,2,2,2,3,4,5,6,7,8,9]
# freq = {}
# for num in numbers:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)



# 12. Count Frequency of Characters
# text = "charr"
# freq = {}
# for char in text:
#     if char not in freq:
#         freq[char] = 1
#     else:
#         freq[char] += 1
# print(freq)


# 13. Merge Two Dictionaries
# dict1 = {"a": 10, "b": 20}
# dict2 = {"c": 30, "d": 40}
# dict1.update(dict2)
# print(dict1)


# 14. Reverse Key-Value Pairs

# data = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }
# reversed_dict = {}
# for key, value in data.items():
#     reversed_dict[value] = key
# print(reversed_dict)




# 15. Sort Dictionary by Keys

# data = {
#     "c": 30,
#     "a": 10,
#     "b": 20
# }

# for key in sorted(data):
#     print(key, data[key])



# 16. Combine Dictionaries with Common Keys
#
# dict1 = {"a": 10, "b": 20}
# dict2 = {"b": 30, "c": 40}
#
# result = {}
#
# for key in set(dict1) | set(dict2):
#     result[key] = dict1.get(key, 0) + dict2.get(key, 0)
#
# print(result)



# 17. Find Duplicate Values
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30
# }
# duplicates = []
# for value in data.values():
#     if list(data.values()).count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
# print(duplicates)



# 18. Group Words by First Letter
# words = ["apple", "ant", "banana", "ball"]
# result = {}
# for word in words:
#     first = word[0]
#     if first not in result:
#         result[first] = []
#     result[first].append(word)
# print(result)




# 19. Find Most Frequent Character
# Solution
# text = "banana"
#
# freq = {}
#
# for char in text:
#     freq[char] = freq.get(char, 0) + 1
#
# most_frequent = max(freq, key=freq.get)
#
# print(most_frequent)



# 20. Nested Dictionary Traversal
#
# students = {
#     "Rahul": {"age": 21, "marks": 85},
#     "Priya": {"age": 20, "marks": 90}
# }
#
# for name, details in students.items():
#     print(name, details)