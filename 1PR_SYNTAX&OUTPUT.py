# 1
print("Hello World")
# Output: Hello World
# Explanation: Simple string print hota hai

# 2
print("Hello")
print("World")
# Output:
# Hello
# World
# Explanation: Har print new line me output deta hai

# 3
print("Hello", "World")
# Output: Hello World
# Explanation: Comma default space add karta hai

# 4
print("Hello" + "World")
# Output: HelloWorld
# Explanation: + strings ko join karta hai (no space)

# 5
print("Hello" + " World")
# Output: Hello World
# Explanation: Space manually add kiya

# 6
print(10)
# Output: 10
# Explanation: Integer directly print hota hai

# 7
print(10, 20, 30)
# Output: 10 20 30
# Explanation: Multiple values space se print hote hain

# 8
print("10 + 20")
# Output: 10 + 20
# Explanation: String hai, calculate nahi hoga

# 9
print(10 + 20)
# Output: 30
# Explanation: Numeric addition hoti hai

# 10
print("Hello", end=" ")
print("World")
# Output: Hello World
# Explanation: end=" " next print ko same line me lata hai

# 11
print("A", "B", "C", sep="-")
# Output: A-B-C
# Explanation: sep custom separator define karta hai

# 12
print("Python", "is", "fun", sep="*")
# Output: Python*is*fun
# Explanation: separator "*" use hua

# 13
print("Hi", end="")
print("There")
# Output: HiThere
# Explanation: end="" newline remove karta hai

# 14
print("Line1\nLine2")
# Output:
# Line1
# Line2
# Explanation: \n new line deta hai

# 15
print("Hello\tWorld")
# Output: Hello    World
# Explanation: \t tab space deta hai

# 16
print("Sum:", 5+5)
# Output: Sum: 10
# Explanation: String + calculation mix ho sakta hai

# 17
print("Age:", 20, "Years")
# Output: Age: 20 Years
# Explanation: Multiple values combine hote hain

# 18
print("A" * 5)
# Output: AAAAA
# Explanation: String repeat hota hai

# 19
print(5 * "A")
# Output: AAAAA
# Explanation: Same repetition rule

# 20
print("Hello" * 2)
# Output: HelloHello
# Explanation: String duplicate hota hai

# 21
print("Hello" + str(10))
# Output: Hello10
# Explanation: int ko string me convert kiya

# 22
print(int("10") + 5)
# Output: 15
# Explanation: String ko int me convert kiya

# 23
print("3" * 3)
# Output: 333
# Explanation: String repeat hota hai

# 24
print(3 * 3)
# Output: 9
# Explanation: Numeric multiplication

# 25
print("Hello", 5, 6.7)
# Output: Hello 5 6.7
# Explanation: Different data types print ho sakte hain

# 26
print("Value =", 10)
# Output: Value = 10
# Explanation: Label + value print

# 27
print("x =", 5, "y =", 10)
# Output: x = 5 y = 10
# Explanation: Multiple labels print

# 28
print("Python\n" * 2)
# Output:
# Python
# Python
# Explanation: string repeat + newline

# 29
print("Hi" + "5")
# Output: Hi5
# Explanation: string concatenation

# 30
print("Hi" + str(5))
# Output: Hi5
# Explanation: int → string conversion

# 31
print(bool("Hello"))
# Output: True
# Explanation: Non-empty string = True

# 32
print(bool(""))
# Output: False
# Explanation: Empty string = False

# 33
print("True:", True)
# Output: True: True
# Explanation: Boolean print hota hai

# 34
print(False, True)
# Output: False True
# Explanation: Boolean values print

# 35
print("5 > 3 =", 5 > 3)
# Output: 5 > 3 = True
# Explanation: Comparison result True

# 36
print("Hello", end="***")
print("World")
# Output: Hello***World
# Explanation: Custom end use hua

# 37
print("A", "B", "C", sep="", end="!")
# Output: ABC!
# Explanation: No separator + custom end

# 38
print("Sum =", 2 + 3 * 4)
# Output: Sum = 14
# Explanation: BODMAS rule follow hota hai

# 39
print((2 + 3) * 4)
# Output: 20
# Explanation: Brackets priority change karte hain

# 40
print("Hello", "\nWorld")
# Output:
# Hello
# World
# Explanation: newline string me diya

# 41
print("Name:", "John", sep="--")
# Output: Name:--John
# Explanation: separator change

# 42
print("Hi", end="\n\n")
print("There")
# Output:
# Hi
#
# There
# Explanation: extra blank line add hua

# 43
print("Hello\\World")
# Output: Hello\World
# Explanation: \\ ek single slash print karta hai

# 44
print("\"Hello\"")
# Output: "Hello"
# Explanation: \" quotes print karne ke liye

# 45
print('It\'s Python')
# Output: It's Python
# Explanation: escape character use hua

# 46
print(10 / 2)
# Output: 5.0
# Explanation: / always float deta hai

# 47
print(10 // 3)
# Output: 3
# Explanation: floor division integer deta hai

# 48
print(10 % 3)
# Output: 1
# Explanation: remainder milta hai

# 49
print(2 ** 3)
# Output: 8
# Explanation: power (2^3)

# 50
print("Result:", 10 > 5 and 5 < 2)
# Output: Result: False
# Explanation: AND me dono condition True honi chahiye