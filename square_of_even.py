numbers = [4, 7, 10, 13, 16, 19, 22]

square_list = []

for char in numbers:
    if char % 2 == 0:
        char = char ** 2
        square_list.append(char)
print(square_list)