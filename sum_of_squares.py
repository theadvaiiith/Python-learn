numbers = [12, 5, 8, 21, 14, 7, 18]

total = 0

for char in numbers:
    if char % 2 == 0:
        char = char ** 2
        total = total + char
print(total)
    