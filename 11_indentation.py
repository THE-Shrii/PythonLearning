# =========================================================
# 🐍 PYTHON NOTES: INDENTATION
# =========================================================


# =========================================================
# 📌 1. DEFINITION
# =========================================================

# Indentation:
# Indentation means giving spaces at the beginning of a line of code.

# In Python, indentation is used to define blocks of code.


# =========================================================
# 📌 2. WHY INDENTATION IS IMPORTANT
# =========================================================

# Python does NOT use {} like other languages.
# It uses indentation to understand which code belongs to which block.


# =========================================================
# 📌 3. BASIC EXAMPLE
# =========================================================

x = 10

if x > 5:
    print("Greater")   # Indented → inside if block

print("Done")          # Not indented → outside block

# Output:
# Greater
# Done


# =========================================================
# 📌 4. WRONG INDENTATION (ERROR)
# =========================================================

# if x > 5:
# print("Error")   ❌ IndentationError

# Python expects indentation after if


# =========================================================
# 📌 5. INDENTATION IN IF-ELSE
# =========================================================

x = 3

if x > 5:
    print("Big")
else:
    print("Small")

# Output:
# Small


# =========================================================
# 📌 6. INDENTATION IN LOOPS
# =========================================================

for i in range(3):
    print(i)

print("Loop End")

# Output:
# 0
# 1
# 2
# Loop End


# =========================================================
# 📌 7. NESTED INDENTATION
# =========================================================

x = 10

if x > 5:
    print("Level 1")

    if x > 8:
        print("Level 2")

# Output:
# Level 1
# Level 2


# =========================================================
# 📌 8. STANDARD RULE (VERY IMPORTANT)
# =========================================================

# Use 4 spaces for indentation (recommended)

if True:
    print("Correct Indentation")


# =========================================================
# 📌 9. COMMON MISTAKES
# =========================================================

# ❌ Mixing tabs and spaces
# ❌ Missing indentation
# ❌ Extra indentation


# =========================================================
# 📌 10. REAL-LIFE LOGIC
# =========================================================

marks = 80

if marks >= 50:
    print("Pass")
    print("Good Job")   # same block

print("End")

# Output:
# Pass
# Good Job
# End


# =========================================================
# 🎯 END OF NOTES
# =========================================================