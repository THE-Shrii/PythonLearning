# =========================================================
# 🐍 FILE I/O PRACTICE SET (40 QUESTIONS)
# =========================================================


# =========================================================
# 📌 Q1: Read entire file
# =========================================================
with open("demo.txt", "r") as f:
    print(f.read())
# Output: (file content)


# =========================================================
# 📌 Q2: Read first line
# =========================================================
with open("demo.txt", "r") as f:
    print(f.readline())
# Output: First line


# =========================================================
# 📌 Q3: Read all lines as list
# =========================================================
with open("demo.txt", "r") as f:
    print(f.readlines())
# Output: ['line1\n', 'line2\n']


# =========================================================
# 📌 Q4: Write to file
# =========================================================
with open("demo.txt", "w") as f:
    f.write("Hello")
# Output: File contains Hello


# =========================================================
# 📌 Q5: Append data
# =========================================================
with open("demo.txt", "a") as f:
    f.write("\nNew Line")
# Output: Adds new line


# =========================================================
# 📌 Q6: Count characters
# =========================================================
with open("demo.txt", "r") as f:
    print(len(f.read()))
# Output: number of characters


# =========================================================
# 📌 Q7: Count lines
# =========================================================
with open("demo.txt", "r") as f:
    print(len(f.readlines()))
# Output: number of lines


# =========================================================
# 📌 Q8: Count words
# =========================================================
with open("demo.txt", "r") as f:
    print(len(f.read().split()))
# Output: number of words


# =========================================================
# 📌 Q9: Copy file
# =========================================================
with open("demo.txt", "r") as f1:
    with open("copy.txt", "w") as f2:
        f2.write(f1.read())


# =========================================================
# 📌 Q10: Read line by line
# =========================================================
with open("demo.txt", "r") as f:
    for line in f:
        print(line.strip())


# =========================================================
# 📌 Q11: Check file exists
# =========================================================
import os
print(os.path.exists("demo.txt"))
# Output: True/False


# =========================================================
# 📌 Q12: Delete file
# =========================================================
import os
# os.remove("demo.txt")


# =========================================================
# 📌 Q13: Write multiple lines
# =========================================================
lines = ["A\n", "B\n", "C\n"]
with open("demo.txt", "w") as f:
    f.writelines(lines)


# =========================================================
# 📌 Q14: Read specific characters
# =========================================================
with open("demo.txt", "r") as f:
    print(f.read(5))


# =========================================================
# 📌 Q15: File cursor position
# =========================================================
with open("demo.txt", "r") as f:
    print(f.tell())


# =========================================================
# 📌 Q16: Move cursor
# =========================================================
with open("demo.txt", "r") as f:
    f.seek(2)
    print(f.read())


# =========================================================
# 📌 Q17: Check readable
# =========================================================
with open("demo.txt", "r") as f:
    print(f.readable())


# =========================================================
# 📌 Q18: Check writable
# =========================================================
with open("demo.txt", "w") as f:
    print(f.writable())


# =========================================================
# 📌 Q19: Append user input
# =========================================================
text = input("Enter text: ")
with open("demo.txt", "a") as f:
    f.write(text)


# =========================================================
# 📌 Q20: Convert file to uppercase
# =========================================================
with open("demo.txt", "r") as f:
    data = f.read()

with open("demo.txt", "w") as f:
    f.write(data.upper())


# =========================================================
# 📌 Q21–Q30 INTERMEDIATE
# =========================================================

# Q21: Count vowels
with open("demo.txt", "r") as f:
    data = f.read()
    print(sum(1 for ch in data if ch in "aeiou"))


# Q22: Replace word
with open("demo.txt", "r") as f:
    data = f.read()

data = data.replace("old", "new")

with open("demo.txt", "w") as f:
    f.write(data)


# Q23: Reverse file content
with open("demo.txt", "r") as f:
    data = f.read()

with open("demo.txt", "w") as f:
    f.write(data[::-1])


# Q24: Merge two files
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    data = f1.read() + f2.read()

with open("merge.txt", "w") as f:
    f.write(data)


# Q25: Copy line by line
with open("demo.txt", "r") as f1, open("copy.txt", "w") as f2:
    for line in f1:
        f2.write(line)


# Q26: Remove blank lines
with open("demo.txt", "r") as f:
    lines = f.readlines()

with open("demo.txt", "w") as f:
    for line in lines:
        if line.strip():
            f.write(line)


# Q27: Count specific word
with open("demo.txt", "r") as f:
    print(f.read().count("python"))


# Q28: Create file if not exists
open("new.txt", "a").close()


# Q29: Read binary file
with open("image.jpg", "rb") as f:
    data = f.read()


# Q30: Write binary file
with open("copy.jpg", "wb") as f:
    f.write(data)


# =========================================================
# 📌 Q31–Q40 ADVANCED
# =========================================================

# Q31: Longest line
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(max(lines, key=len))


# Q32: Shortest line
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(min(lines, key=len))


# Q33: Line count without newline
with open("demo.txt", "r") as f:
    print(len([l for l in f if l.strip()]))


# Q34: Number file copy
with open("demo.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())


# Q35: Swap file content
with open("file1.txt") as f1, open("file2.txt") as f2:
    d1, d2 = f1.read(), f2.read()

with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write(d2)
    f2.write(d1)


# Q36: Find longest word
with open("demo.txt", "r") as f:
    words = f.read().split()
    print(max(words, key=len))


# Q37: Remove punctuation
import string
with open("demo.txt", "r") as f:
    data = f.read()

clean = "".join(ch for ch in data if ch not in string.punctuation)

with open("demo.txt", "w") as f:
    f.write(clean)


# Q38: Count digits
with open("demo.txt", "r") as f:
    print(sum(ch.isdigit() for ch in f.read()))


# Q39: Count uppercase
with open("demo.txt", "r") as f:
    print(sum(ch.isupper() for ch in f.read()))


# Q40: File size
import os
print(os.path.getsize("demo.txt"))
# Output: size in bytes


# =========================================================
# 🎯 END OF PRACTICE SET
# =========================================================