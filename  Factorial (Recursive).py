# 2. Write a recursive function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))  # 120
print(factorial(0))  # 1
print(factorial(16))  # 1

