
# ================= BASIC (1–10) =================

# Q1. Match a number
x = 2
match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")
# Explanation:
# x = 2 → matches case 2
# Output: Two


# Q2. Match string
day = "Mon"
match day:
    case "Mon":
        print("Monday")
    case "Tue":
        print("Tuesday")
# Explanation:
# string comparison → "Mon" matched
# Output: Monday


# Q3. Default case
x = 5
match x:
    case 1:
        print("One")
    case _:
        print("Default")
# Explanation:
# no match → _ (default case)
# Output: Default


# Q4. Multiple cases
x = 3
match x:
    case 1 | 2:
        print("Small")
    case 3 | 4:
        print("Medium")
# Explanation:
# 3 matches second group
# Output: Medium


# Q5. Match boolean
val = True
match val:
    case True:
        print("Yes")
    case False:
        print("No")
# Output: Yes


# Q6. Match even/odd using guard
x = 4
match x:
    case n if n % 2 == 0:
        print("Even")
    case _:
        print("Odd")
# Explanation:
# condition checked using 'if'
# Output: Even


# Q7. Match negative
x = -2
match x:
    case n if n < 0:
        print("Negative")
# Output: Negative


# Q8. Match range
x = 15
match x:
    case n if 1 <= n <= 10:
        print("1-10")
    case n if 11 <= n <= 20:
        print("11-20")
# Output: 11-20


# Q9. Match multiple types
x = "hello"
match x:
    case int():
        print("Integer")
    case str():
        print("String")
# Output: String


# Q10. Match None
x = None
match x:
    case None:
        print("No value")
# Output: No value


# ================= LIST / TUPLE (11–20) =================

# Q11. Match list
lst = [1,2]
match lst:
    case [1,2]:
        print("Matched")
# Output: Matched


# Q12. Match list length
lst = [1,2,3]
match lst:
    case [a,b,c]:
        print(a,b,c)
# Output: 1 2 3


# Q13. Match first element
lst = [1,5,6]
match lst:
    case [1, *rest]:
        print(rest)
# Output: [5,6]


# Q14. Match last element
lst = [4,5,6]
match lst:
    case [*start, 6]:
        print(start)
# Output: [4,5]


# Q15. Match tuple
t = (1,2)
match t:
    case (1,2):
        print("Tuple match")
# Output: Tuple match


# Q16. Tuple unpacking
t = (3,4)
match t:
    case (a,b):
        print(a+b)
# Output: 7


# Q17. Nested match
t = (1,(2,3))
match t:
    case (1,(a,b)):
        print(a,b)
# Output: 2 3


# Q18. Ignore values
lst = [1,2,3]
match lst:
    case [_,2,_]:
        print("Middle is 2")
# Output: Middle is 2


# Q19. Match empty list
lst = []
match lst:
    case []:
        print("Empty")
# Output: Empty


# Q20. Match variable length
lst = [1,2,3,4]
match lst:
    case [1,*rest]:
        print(len(rest))
# Output: 3


# ================= DICTIONARY (21–30) =================

# Q21. Match dict keys
d = {"name":"A"}
match d:
    case {"name": n}:
        print(n)
# Output: A


# Q22. Match multiple keys
d = {"x":1,"y":2}
match d:
    case {"x":a,"y":b}:
        print(a+b)
# Output: 3


# Q23. Partial match
d = {"x":5,"y":10}
match d:
    case {"x":a}:
        print(a)
# Output: 5


# Q24. Match with condition
d = {"age":20}
match d:
    case {"age": a} if a >= 18:
        print("Adult")
# Output: Adult


# Q25. Missing key
d = {}
match d:
    case {"x":_}:
        print("Has x")
    case _:
        print("No key")
# Output: No key


# Q26. Match nested dict
d = {"a":{"b":2}}
match d:
    case {"a":{"b":x}}:
        print(x)
# Output: 2


# Q27. Ignore extra keys
d = {"x":1,"y":2,"z":3}
match d:
    case {"x":1, **rest}:
        print(rest)
# Output: {'y':2,'z':3}


# Q28. Dict with list
d = {"nums":[1,2]}
match d:
    case {"nums":[a,b]}:
        print(a*b)
# Output: 2


# Q29. Match exact dict
d = {"a":1}
match d:
    case {"a":1}:
        print("Exact")
# Output: Exact


# Q30. Default dict case
d = {"b":2}
match d:
    case {"a":_}:
        print("A exists")
    case _:
        print("Other dict")
# Output: Other dict


# ================= ADVANCED (31–50) =================

# Q31. Match class type
x = 10
match x:
    case int():
        print("Integer")
# Output: Integer


# Q32. Match string pattern
s = "hi"
match s:
    case "hi" | "hello":
        print("Greeting")
# Output: Greeting


# Q33. Guard condition
x = 7
match x:
    case n if n > 5:
        print("Greater than 5")
# Output: Greater than 5


# Q34. Multiple guards
x = 12
match x:
    case n if n%2==0 and n>10:
        print("Even >10")
# Output: Even >10


# Q35. Match nested list
lst = [[1,2],[3,4]]
match lst:
    case [[a,b],[c,d]]:
        print(a+b+c+d)
# Output: 10


# Q36. Match string length
s = "abc"
match s:
    case str() if len(s)==3:
        print("Length 3")
# Output: Length 3


# Q37. Match mixed list
lst = [1,"a"]
match lst:
    case [int(), str()]:
        print("Mixed types")
# Output: Mixed types


# Q38. Match None or value
x = None
match x:
    case None:
        print("None")
# Output: None


# Q39. Match with alias
x = 5
match x:
    case n:
        print(n*2)
# Output: 10


# Q40. Match float
x = 3.5
match x:
    case float():
        print("Float")
# Output: Float


# Q41. Match boolean
x = False
match x:
    case False:
        print("False case")
# Output: False case


# Q42. Match range groups
x = 25
match x:
    case n if n < 10:
        print("Small")
    case n if n < 30:
        print("Medium")
# Output: Medium


# Q43. Match tuple size
t = (1,2,3)
match t:
    case (a,b,c):
        print(a*b*c)
# Output: 6


# Q44. Ignore middle values
t = (1,2,3)
match t:
    case (1,_,3):
        print("Matched pattern")
# Output: Matched pattern


# Q45. Match list start/end
lst = [1,2,3]
match lst:
    case [1,*_,3]:
        print("Start & End match")
# Output: Start & End match


# Q46. Match string type
x = "python"
match x:
    case str():
        print(len(x))
# Output: 6


# Q47. Match zero
x = 0
match x:
    case 0:
        print("Zero")
# Output: Zero


# Q48. Match any number
x = 100
match x:
    case _:
        print("Anything")
# Output: Anything


# Q49. Match even/odd
x = 9
match x:
    case n if n%2==0:
        print("Even")
    case _:
        print("Odd")
# Output: Odd


# Q50. Final mixed case
x = [1,2,3]
match x:
    case [1, *rest]:
        print(sum(rest))
# Output: 5