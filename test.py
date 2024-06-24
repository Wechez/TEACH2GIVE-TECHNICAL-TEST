def reverse_integer(num):
    reversed_num = int(str(abs(num))[::-1])
    return reversed_num if num >= 0 else -reversed_num

print(reverse_integer(50))  # 5
print(reverse_integer(-12))  # -21
print(reverse_integer(123))  # 321
