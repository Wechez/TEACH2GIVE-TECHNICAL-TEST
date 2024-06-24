# 5. Design a function that takes a list of integers as input. The function should return True if the list contains two consecutive threes (3 next to a 3) anywhere within the list. Otherwise, it should return False. For example, the function should return True for [1, 3, 3] and False for [1, 3, 1, 3].
def has_consecutive_threes(ints):
    for i in range(len(ints) - 1):
        if ints[i] == 3 and ints[i + 1] == 3:
            return True
    return False

print(has_consecutive_threes([1, 3, 3]))  # True
print(has_consecutive_threes([1, 3, 1, 3]))  # False
print(has_consecutive_threes([3, 3, 3]))  # True
