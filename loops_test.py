    # 1. Print Numbers from 1 to 10
    # for i in range(1, 11):
    #     print(i)


    # 2.Print Even Numbers from 1 to 20
    # for i in range(21):
    #     if i % 2 == 0:
    #         print(i)


    # 3. Print Odd Numbers from 1 to 20
    # for i in range(21):
    #     if i % 2 != 0:
    #         print(i)


    # 4. Sum of First 10 Natural Numbers
    # total = 0
    # for i  in range (1,11):
    #     total = total + i
    # print(total)


    # 5.Print table of 5.
    # num = 5
    # for i in range(11):
    #     print(f" {num} X {i} = {num*i}")



    # 6. Factorial of a Number
    # num = 5
    # fact = 1
    #
    # for i in range(1, num + 1):
    #     fact *= i
    #
    # print(fact)


    # 7. Count Digits in a Number
    # dig = 0
    # num = 123
    # while num > 0:
    #     dig = dig + 1
    #     num //= 10
    #
    # print(dig)


    # 8. Reverse a Number
    # num = 1234
    # reverse = 0
    #
    # while num > 0:
    #     digit = num % 10
    #     reverse = reverse * 10 + digit
    #     num //= 10
    #
    # print(reverse)


    # 9. Sum of Digits
    # num = 1234
    # total = 0
    #
    # while num > 0:
    #     total += num % 10
    #     num //= 10
    #
    # print(total)



    # 10. Check Prime Number


    # num = 13
    #
    # is_prime = True
    #
    # for i in range(2, num):
    #     if num % i == 0:
    #         is_prime = False
    #         break
    #
    # if is_prime:
    #     print("Prime")
    # else:
    #     print("Not Prime")







    # 11. Find Factors of a Number
    # num = 12
    #
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         print(i)


    # 12. Fibonacci Series
    # a = 0
    # b = 1
    #
    # for i in range(10):
    #     print(a)
    #     a, b = b, a + b





    # 13. Armstrong Number
    # Check whether 153 is an Armstrong number.
    #
    # num = 153
    # temp = num
    # total = 0
    #
    # while temp > 0:
    #     digit = temp % 10
    #     total += digit ** 3
    #     temp //= 10
    #
    # if total == num:
    #     print("Armstrong")
    # else:
    #     print("Not Armstrong")



    # 14. Palindrome Number

    # num = 121
    # temp = num
    # reverse = 0
    #
    # while temp > 0:
    #     digit = temp % 10
    #     reverse = reverse * 10 + digit
    #     temp //= 10
    #
    # if num == reverse:
    #     print("Palindrome")
    # else:
    #     print("Not Palindrome")



    # 15. Find Largest Digit

    # num = 53872
    # largest = 0
    #
    # while num > 0:
    #     digit = num % 10
    #
    #     if digit > largest:
    #         largest = digit
    #
    #     num //= 10
    #
    # print(largest)



    # 16. Square Pattern
    #
    # for i in range(5):
    #     for j in range(5):
    #         print("*", end=" ")
    #     print()



    # Right Triangle Pattern

    # for i in range(1, 6):
        # print("*" * i)



    # 18. Inverted Triangle
    # for i in range(5, 0, -1):
    #     print("*" * i)