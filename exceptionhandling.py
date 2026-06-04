# ==========================================
# PYTHON EXCEPTION HANDLING INTERVIEW QUESTIONS
# ==========================================

# ------------------------------------------
# 1. Handle ZeroDivisionError
# ------------------------------------------

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

# Output:
# Cannot divide by zero


# ------------------------------------------
# 2. Handle ValueError
# ------------------------------------------

try:
    num = int("abc")
    print(num)

except ValueError:
    print("Invalid Input")

# Output:
# Invalid Input


# ------------------------------------------
# 3. Handle IndexError
# ------------------------------------------

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index Out of Range")

# Output:
# Index Out of Range


# ------------------------------------------
# 4. Handle KeyError
# ------------------------------------------

student = {
    "name": "Rahul",
    "age": 21
}

try:
    print(student["city"])

except KeyError:
    print("Key Not Found")

# Output:
# Key Not Found


# ------------------------------------------
# 5. Handle NameError
# ------------------------------------------

try:
    print(age)

except NameError:
    print("Variable Not Defined")

# Output:
# Variable Not Defined


# ------------------------------------------
# 6. Multiple Except Blocks
# ------------------------------------------

try:
    num = int("abc")
    result = 10 / num

except ValueError:
    print("Invalid Value")

except ZeroDivisionError:
    print("Cannot Divide By Zero")

# Output:
# Invalid Value


# ------------------------------------------
# 7. Generic Exception Handling
# ------------------------------------------

try:
    print(10 / 0)

except Exception as e:
    print("Error:", e)

# Output:
# Error: division by zero


# ------------------------------------------
# 8. Using else Block
# ------------------------------------------

try:
    num = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Executed Successfully")

# Output:
# Executed Successfully


# ------------------------------------------
# 9. Using finally Block
# ------------------------------------------

try:
    print("Hello")

except:
    print("Error")

finally:
    print("Always Executes")

# Output:
# Hello
# Always Executes


# ------------------------------------------
# 10. else + finally Together
# ------------------------------------------

try:
    num = 10 / 2

except:
    print("Error")

else:
    print("Success")

finally:
    print("Finished")

# Output:
# Success
# Finished


# ------------------------------------------
# 11. File Handling Exception
# ------------------------------------------

try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File Not Found")

finally:
    print("Closing Resources")

# Output:
# File Not Found
# Closing Resources


# ------------------------------------------
# 12. Raise Exception Manually
# ------------------------------------------

age = 15

try:
    if age < 18:
        raise ValueError("Age Must Be 18+")

except ValueError as e:
    print(e)

# Output:
# Age Must Be 18+


# ------------------------------------------
# 13. Custom Exception
# ------------------------------------------

class InvalidAgeError(Exception):
    pass

try:
    age = 15

    if age < 18:
        raise InvalidAgeError("Not Eligible")

except InvalidAgeError as e:
    print(e)

# Output:
# Not Eligible


# ------------------------------------------
# 14. ATM Withdrawal System
# ------------------------------------------

balance = 5000

try:
    amount = int(input("Enter Amount: "))

    if amount > balance:
        raise ValueError("Insufficient Balance")

    balance -= amount

    print("Remaining Balance:", balance)

except ValueError as e:
    print(e)


# ------------------------------------------
# 15. Password Validation
# ------------------------------------------

try:
    password = input("Enter Password: ")

    if len(password) < 8:
        raise ValueError("Password Too Short")

    print("Password Accepted")

except ValueError as e:
    print(e)


# ------------------------------------------
# 16. Login System
# ------------------------------------------

try:
    username = input("Enter Username: ")

    if username == "":
        raise ValueError("Username Cannot Be Empty")

    print("Login Successful")

except ValueError as e:
    print(e)


# ------------------------------------------
# 17. Nested Try Except
# ------------------------------------------

try:

    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Exception")

except:
    print("Outer Exception")

# Output:
# Inner Exception


# ------------------------------------------
# 18. Handle Multiple Exceptions Together
# ------------------------------------------

try:
    num = int(input("Enter Number: "))
    result = 10 / num

except (ValueError, ZeroDivisionError):
    print("Invalid Input Or Division By Zero")


# ------------------------------------------
# 19. Predict Output Question
# ------------------------------------------

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Error")

finally:
    print("Done")

# Output:
# Error
# Done


# ------------------------------------------
# 20. Calculator Using Exception Handling
# ------------------------------------------

try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    print("Division =", num1 / num2)

except ValueError:
    print("Please Enter Valid Numbers")

except ZeroDivisionError:
    print("Cannot Divide By Zero")


# ==========================================
# MOST ASKED INTERVIEW QUESTIONS
# ==========================================

# 1. What is Exception Handling?
# 2. Why do we use try-except?
# 3. Difference between Error and Exception?
# 4. Difference between except and finally?
# 5. Difference between else and finally?
# 6. What is raise keyword?
# 7. What is custom exception?
# 8. What is Exception class?
# 9. How to handle multiple exceptions?
# 10. What is nested try-except?


# ==========================================
# MOST IMPORTANT OUTPUT QUESTIONS
# ==========================================

# Question 1
try:
    print("Hello")
except:
    print("Error")
else:
    print("Success")

# Output:
# Hello
# Success


# Question 2
try:
    print(int("100"))
except:
    print("Error")
finally:
    print("Finished")

# Output:
# 100
# Finished


# Question 3
try:
    print(x)
except NameError:
    print("Variable Not Defined")

# Output:
# Variable Not Defined