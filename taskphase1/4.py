input_string = input("Enter a string: ")
sorted_string = ""

while input_string != "":
    min_char = input_string[0]

    for char in input_string:
        if char < min_char:
            min_char = char

    sorted_string += min_char

    found = False
    new_string = ""
    for char in input_string:
        if char == min_char and not found:
            found = True
            continue
        new_string += char

    input_string = new_string

print("Sorted string:", sorted_string)
