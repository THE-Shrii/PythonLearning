# 1. Create a dictionary
d = {"name": "John", "age": 25}
# Output: {'name': 'John', 'age': 25}

# 2. Access value using key
print(d["name"])
# Output: John

# 3. Use get() method
print(d.get("age"))
# Output: 25

# 4. Add new key-value pair
d["city"] = "Delhi"
# Output: {'name':'John','age':25,'city':'Delhi'}

# 5. Update value
d["age"] = 30
# Output: age = 30

# 6. Remove item using pop()
d.pop("city")

# 7. Remove last inserted item
d.popitem()

# 8. Delete key
del d["name"]

# 9. Clear dictionary
d.clear()
# Output: {}

# 10. Create empty dictionary
d2 = {}

# 11. Dictionary with mixed types
d3 = {"num": 1, "list": [1,2], "bool": True}

# 12. Check key exists
print("num" in d3)
# Output: True

# 13. Get all keys
print(d3.keys())

# 14. Get all values
print(d3.values())

# 15. Get all items
print(d3.items())

# 16. Loop through keys
for k in d3:
    print(k)

# 17. Loop through values
for v in d3.values():
    print(v)

# 18. Loop through key-value pairs
for k,v in d3.items():
    print(k,v)

# 19. Copy dictionary
d4 = d3.copy()

# 20. Create dict using dict()
d5 = dict(a=1, b=2)

# 21. Nested dictionary
d6 = {"a": {"b": 2}}
print(d6["a"]["b"])
# Output: 2

# 22. Update dictionary
d5.update({"c":3})

# 23. Merge dictionaries
d7 = {**d5, **d3}

# 24. Length of dictionary
print(len(d3))

# 25. Remove key safely
d3.pop("x", None)

# 26. Set default value
d3.setdefault("new", 100)

# 27. Create dict from keys
keys = ["a","b","c"]
d8 = dict.fromkeys(keys, 0)
# Output: {'a':0,'b':0,'c':0}

# 28. Access non-existing key
print(d3.get("unknown"))
# Output: None

# 29. Dictionary comprehension
sq = {i: i*i for i in range(5)}
# Output: {0:0,1:1,2:4,3:9,4:16}

# 30. Filter dictionary
filtered = {k:v for k,v in sq.items() if v > 5}
# Output: {3:9,4:16}

# 31. Count frequency
lst = [1,2,2,3]
freq = {}
for i in lst:
    freq[i] = freq.get(i,0)+1
print(freq)
# Output: {1:1,2:2,3:1}

# 32. Find max value
print(max(sq.values()))

# 33. Find key with max value
print(max(sq, key=sq.get))

# 34. Sort dictionary by keys
print(dict(sorted(sq.items())))

# 35. Sort by values
print(dict(sorted(sq.items(), key=lambda x: x[1])))

# 36. Reverse dictionary
rev = {v:k for k,v in d5.items()}
print(rev)

# 37. Check equality
print({"a":1} == {"a":1})
# Output: True

# 38. Nested loop in dict
d9 = {"a":[1,2], "b":[3,4]}
for k,v in d9.items():
    for i in v:
        print(i)

# 39. Remove duplicates using dict
lst2 = [1,2,2,3]
unique = list(dict.fromkeys(lst2))
print(unique)
# Output: [1,2,3]

# 40. Count characters in string
word = "hello"
count = {}
for ch in word:
    count[ch] = count.get(ch,0)+1
print(count)
# Output: {'h':1,'e':1,'l':2,'o':1}

# 41. Convert list of tuples to dict
pairs = [("a",1),("b",2)]
print(dict(pairs))

# 42. Check if dict is empty
print(len(d2) == 0)

# 43. Delete entire dictionary
del d2

# 44. Access nested safely
print(d6.get("a", {}).get("b"))

# 45. Merge using update
d10 = {"x":1}
d10.update({"y":2})

# 46. Multiply values
d11 = {"a":2,"b":3}
res = {k:v*2 for k,v in d11.items()}
print(res)
# Output: {'a':4,'b':6}

# 47. Extract keys as list
keys_list = list(d11.keys())

# 48. Extract values as list
values_list = list(d11.values())

# 49. Create dict from two lists
k = ["a","b"]
v = [1,2]
print(dict(zip(k,v)))
# Output: {'a':1,'b':2}

# 50. Check all values > 0
print(all(v > 0 for v in d11.values()))
# Output: True