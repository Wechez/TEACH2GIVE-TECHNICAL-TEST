# 4. Design a function that determines whether a given string is a pangram. A pangram is a sentence or phrase containing every letter of the alphabet at least once. Punctuation and case are typically ignored. For example, the string "The quick brown fox jumps over the lazy dog" is a pangram, while "Hello, world!" is not.
def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s_lower = s.lower()

    for char in alphabet:
        if char not in s_lower:
            return False
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Hello, world!"))  # False
print(is_pangram("abcdefghijklmnopqrstuvwxyz"))  # True

