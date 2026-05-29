# 1. Print String Length
#
# Question:
# Write a program to find the length of a string "Python".
#
# a = "Python"
# print(len(a))

# 2. Type Conversion (String to Integer)
#
# Question:
# Convert "100" into an integer and add 50.

# a = "34"
# b = (int(a))
# print(type(b))



# 3. Uppercase Conversion
#
# Question:
# Convert "hello world" into uppercase.

# a = "hello world"
# print(a.upper())



# 4. Count Vowels in a String
#
# Question:
# Count vowels in "education".

# a = "education"
# vowel = "aeiou"
# vowelcount = 0
#
# for a in vowel:
#     if a in vowel:
#         vowelcount += 1
#
# print(vowelcount)


# 5. String to Float Conversion
#
# Question:
# Convert "45.67" into float and multiply by 2.

# a = '45.67'
# b = float(a) * 2
# print(b)



# 6. Reverse a String
#
# Question:
# Reverse "python".

# a = "Python"
# print(a[::-1])



# 7. Check Palindrome
#
# Question:
# Check if "madam" is a palindrome.

# a = "mad"
# b = a[::-1]
# if a == b:
#     print("The string is plaindrom")
# else:
#     print("The string is not plaindrom")


# 8. Sum of Numbers in String
#
# Question:
# Given "10 20 30", convert and find sum.

# a = "10 20 30"
# number = a.split()
#
# total = 0
# for a in number:
#     total = total + int(a)
# print(total)



# 9. Extract Digits and Convert
#
# Question:
# From "a1b2c3", extract numbers and find their sum.

# text = "a1b2c3"
# total = 0
#
# for char in text:
#     if char.isdigit():
#         total += int(char)
#
# print(total)



# 10. String Formatting + Type Conversion
#
# Question:
# Take input "25" (string age), convert to integer and print:
# "After 5 years, age will be X"

# input1 = input("Enter a number: ")
# age = int(input1)
# print(f"After 5 years, age will be {age+5}")



# 11. Word Count + Type Conversion
#
# Question:
# Count words in "I love Python programming" and convert count to string.

# word = "I love Python programming"
# length = len(word)
# a = (str(length))
# print(a)
# print(type(a))





# 12. Mixed Type Input Processing
#
# Question:
# User input: "10,20,30,40"
# Convert to integers and find average.

# text = "10,20,30,40"
# numbers = text.split(",")
#
# total = 0
# for num in numbers:
#     total += int(num)
#
# average = total / len(numbers)
# print(average)



# Remove Spaces from String
# Question
#
# Remove all spaces from a string.

# text = "I love Python"
#
# result = text.replace(" ", "")
#
# print(result)




# Count Characters Frequency
# Question
#
# Count frequency of each character.


# a = "Shrii"
# freq = {}
#
# for char in a:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
#
# print(freq)





# Find Largest Word in Sentence
# Question
#
# Find the longest word in a sentence.


# a = "PYTHON IS A LANGUAGE"
# words = a.split()
# split() breaks a sentence into separate words using spaces.
# becomes:
# ['I', 'love', 'Python', 'programming']
largest = ""
# create an empty string to store the longest word.

# Loop will run on every word one by one.
# for word in words:
#     if len(word) > len(largest):
#         largest = word
# print(largest)


# Check Anagram
# Question
#
# Check if two strings are anagrams.
#
# Example:
# listen and silent
# str1 = "listen"
# str2 = "silent"
#
# if sorted(str1) == sorted(str2):
#     print("Anagram")
# else:
#     print("Not Anagram")




# First Non-Repeating Character
# Question
#
# Find first non-repeating character.
#
# Solution
# text = "aabbcddee"
#
# for char in text:
#     if text.count(char) == 1:
#         print(char)
#         break




# Remove Duplicate Characters
# Question
#
# Remove duplicate characters from string.

# text = "Programsss"
# data = ""
#
# for char in text:
#     if char not in text:
#         data += char
# print(data)




# Find Duplicate Characters
# Question
#
# Print duplicate characters in string.

# text = "Programmingg"
# duplicates = []
#
# for char in text:
#     if text.count(char) > 1 and  char not in duplicates:
#         duplicates.append(char)
# print(duplicates)






# Capitalize First Letter of Every Word
# Question
#
# Convert:
# "i love python"

# text = "i love python"
# print(text.title())


# Find All Substrings
# Question
# Print all substrings of a string.


# Most Repeated Character
# Question
# Find most repeated character.

# a ="POWEREjokhgfdsdfghjjkhgD"
# max_char  = ""
# max_count = 0
# for char in a:
#     count = a.count(char)
#
#     if count > max_count:
#         max_count = count
#         max_char = char
# print(max_char)



# Check String Contains Only Digits
# Question
#
# Check whether string contains only numbers
# text = "12345"
# if text.isdigit():
#     print("Only Digits")
# else:
#     print("Contains Other Characters")
