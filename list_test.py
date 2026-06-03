# 1. Find Length of a List
# a = [1,2,2]
# print(len(a))


# 2. Find Sum of List Elements
# a = [1,2,3,4]
# tot = 0
# for num in a:
#     tot += num
# print(tot)

# 3. Find Largest Element
# a = [4,6,7,99,900]
# largest = 0
# for num in a:
#     if num > largest:
#         largest = num
# print(largest)


# 4. Find Smallest Element
# a = [98,8,0,-1,3]
# smallest = a[0]
# for num in a:
#     if num < smallest:
#         smallest = num
# print(smallest)


# 5. Count Even and Odd Numbers
# a = [2,4,2,3,5]
# even_count = 0
# odd_count = 0
# for num in a:
#     if  num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f'Even count is : {even_count} , Odd count is: {odd_count}')



# 6. Find Second Largest Element
# a = [0, 2, 4, 9]

# first_largest = float('-inf')
# second_largest = float('-inf')
#
# for num in a:
#     if num > first_largest:
#         second_largest = first_largest
#         first_largest = num
#     elif num > second_largest and num != first_largest:
#         second_largest = num
#
# print(first_largest, second_largest)

# a.sort()
# print(a[-2])


# 7. Reverse a List
# a = [9,8,7]
# print(a[::-1])


# 8. Remove Duplicates
# a = [1,1,1,2,2,4,5,6]
# print(list(set(a)))
# unique = []
# for num in a:
#     if num not in unique:
#         unique.append(num)
# print(unique)


# 9. Check if List is Sorted
# numbers = [10, 20, 30, 40]
# if numbers == sorted(numbers):
#     print("Sorted")
# else:
#     print("Not Sorted")


# 10. Find Average of List
# a = [1,2,3,4]
# average = sum(a) / len(a)
# print(average)


# 11. Find Missing Number

# We use the formula:
#
# 1+2+⋯+n=
# 2
# n(n+1)
# 	​

# numbers = [1, 2, 3, 5]
# n = 5
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(numbers)
# print(expected_sum - actual_sum)



# 12. Find Duplicate Elements
# a = [1,2,3,3,4,4,4,5,44]
# duplicates = []
# for item in a:
#     if item not in duplicates and a.count(item) > 1:
#         duplicates.append(item)
# print(duplicates)


# 13. Find Common Elements in Two Lists
# a = [1,2,3]
# b = [5,4,3]
# common = []
# for num in a:
#     if num in b:
#         common.append(num)
# print(common)


# 14. Rotate List by One Position
# a = [4,3,2,1]
# rotate = [a[-1]] + a[:-1]
# print(rotate)


# 15. Separate Positive and Negative Numbers
# a = [9,3,0,-1,-6,-99,99]
# positive_num = []
# neagtive_num = []
# for num in a :
#     if num > 0 :
#         positive_num.append(num)
#     else:
#         neagtive_num.append(num)
# print(positive_num)
# print(neagtive_num)


# 16. Find Second Smallest Element
# a = [0,9,6,2]
# a.sort()
# print(a[1])

# 17. Find Frequency of Each Element
# a = [8,7,88,88,9,9,0]
# freq = {}
# for num in a:
#     freq[num] = freq.get(num, 0) + 1
# print(freq)


# 18. Merge Two Lists Without Duplicates
# a = [2,2,5]
# b = [5,6,6,8]
# b = (list(set(a + b)))
# b.sort()
# print(b)



# 19. Find Maximum Difference
# numbers = [10, 5, 20, 8]
# print(max(numbers) - min(numbers))


# 20. Move All Zeros to End
# numbers = [1, 0, 2, 0, 3, 4]
#
# result = []
#
# for num in numbers:
#     if num != 0:
#         result.append(num)
#
# zero_count = numbers.count(0)
#
# for i in range(zero_count):
#     result.append(0)
#
# print(result)