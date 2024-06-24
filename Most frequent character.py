#3. Design a function that takes a string or sequence of characters as input and returns the character that appears most frequently.
#Eg 2228869 => '2'
#amazing => 'a' 
def most_frequent_char(s):
    char_count = {}
    max_char = ''
    max_count = 0

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        if char_count[char] > max_count:
            max_char = char
            max_count = char_count[char]

    return max_char

print(most_frequent_char("2228869"))  # '1'
print(most_frequent_char("hello"))  # 'l'
print(most_frequent_char("amazing"))  # 'a'
