# 1. Design a function that reverses the digits of an integer.
# For example, 78 should become 87 and -32 should become -23.

def reverse_integer(num):
    reversed_num = int(str(abs(num))[::-1])
    return reversed_num if num >= 0 else -reversed_num

print(reverse_integer(100))  #1 
print(reverse_integer(-32))  # -23
print(reverse_integer(123))  # 321
