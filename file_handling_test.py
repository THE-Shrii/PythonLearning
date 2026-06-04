# ============================================
# PYTHON FILE HANDLING INTERVIEW QUESTIONS
# ============================================

# --------------------------------------------
# 1. Write data into a file
# --------------------------------------------

with open("data.txt", "w") as file:
    file.write("Hello Python")

# Output in file:
# Hello Python


# --------------------------------------------
# 2. Read complete file
# --------------------------------------------

with open("data.txt", "r") as file:
    content = file.read()

print(content)

# Output:
# Hello Python


# --------------------------------------------
# 3. Append data to a file
# --------------------------------------------

with open("data.txt", "a") as file:
    file.write("\nWelcome")

# Output in file:
# Hello Python
# Welcome


# --------------------------------------------
# 4. Read file line by line
# --------------------------------------------

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# Output:
# Hello Python
# Welcome


# --------------------------------------------
# 5. Count number of lines
# --------------------------------------------

with open("data.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))

# Output:
# Total Lines: 2


# --------------------------------------------
# 6. Count words in file
# --------------------------------------------

with open("data.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total Words:", len(words))

# Output:
# Total Words: 3


# --------------------------------------------
# 7. Count characters in file
# --------------------------------------------

with open("data.txt", "r") as file:
    content = file.read()

print("Characters:", len(content))

# Output:
# Characters: 20 (may vary)


# --------------------------------------------
# 8. Copy one file into another
# --------------------------------------------

with open("data.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("File Copied Successfully")

# Output:
# File Copied Successfully


# --------------------------------------------
# 9. Read first 3 lines
# --------------------------------------------

with open("data.txt", "r") as file:
    for i in range(3):
        print(file.readline().strip())

# Output:
# First three lines (if available)


# --------------------------------------------
# 10. Find longest word in file
# --------------------------------------------

with open("data.txt", "r") as file:
    words = file.read().split()

longest_word = max(words, key=len)

print("Longest Word:", longest_word)

# Output:
# Longest Word: Welcome


# --------------------------------------------
# 11. Handle File Not Found Error
# --------------------------------------------

try:
    with open("abc.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File Not Found")

# Output:
# File Not Found


# --------------------------------------------
# 12. Create file only if it doesn't exist
# --------------------------------------------

try:
    with open("newfile.txt", "x") as file:
        print("File Created")

except FileExistsError:
    print("File Already Exists")


# --------------------------------------------
# 13. Read and Write using r+
# --------------------------------------------

with open("data.txt", "r+") as file:
    print(file.read())
    file.write("\nNew Data")

# Output:
# Existing content displayed
# New Data appended


# --------------------------------------------
# 14. Reverse file content
# --------------------------------------------

with open("data.txt", "r") as file:
    content = file.read()

print(content[::-1])

# Output:
# Reversed content


# --------------------------------------------
# 15. Count frequency of words
# --------------------------------------------

with open("data.txt", "r") as file:
    words = file.read().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# Example Output:
# {'Hello': 1, 'Python': 1, 'Welcome': 1}


# --------------------------------------------
# 16. Merge two files
# --------------------------------------------

with open("file1.txt", "r") as f1:
    data1 = f1.read()

with open("file2.txt", "r") as f2:
    data2 = f2.read()

with open("merged.txt", "w") as f3:
    f3.write(data1)
    f3.write("\n")
    f3.write(data2)

print("Files Merged Successfully")

# Output:
# Files Merged Successfully


# --------------------------------------------
# 17. Search a word in file
# --------------------------------------------

search_word = "Python"

with open("data.txt", "r") as file:
    content = file.read()

if search_word in content:
    print("Word Found")
else:
    print("Word Not Found")

# Output:
# Word Found


# --------------------------------------------
# 18. Replace a word in file
# --------------------------------------------

with open("data.txt", "r") as file:
    content = file.read()

content = content.replace("Python", "Java")

with open("data.txt", "w") as file:
    file.write(content)

print("Word Replaced")

# Output:
# Word Replaced


# --------------------------------------------
# 19. Find file size
# --------------------------------------------

import os

size = os.path.getsize("data.txt")

print("File Size:", size, "bytes")

# Output:
# File Size: xx bytes


# --------------------------------------------
# 20. Delete a file
# --------------------------------------------

import os

if os.path.exists("temp.txt"):
    os.remove("temp.txt")
    print("File Deleted")
else:
    print("File Not Found")

# Output:
# File Deleted
# OR
# File Not Found


# ============================================
# TOP INTERVIEW QUESTIONS
# ============================================

# 1. Read a file
# 2. Write into a file
# 3. Append data
# 4. Count lines
# 5. Count words
# 6. Count characters
# 7. Copy file
# 8. Merge files
# 9. Search word in file
# 10. Replace word in file
# 11. Longest word in file
# 12. File size
# 13. Delete file
# 14. Handle FileNotFoundError
# 15. Difference between r, w, a modes