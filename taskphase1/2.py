input_string = input("Enter a string: ")

chars = list(input_string)

for i in range(len(chars)):
    for j in range(i + 1, len(chars)):
        if chars[j] < chars[i]:
            chars[i], chars[j] = chars[j], chars[i]

sorted_string = "".join(chars)
print("Sorted string:", sorted_string)

char_count = {}
for char in sorted_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char in char_count:
    print(f"'{char}': {char_count[char]}")
