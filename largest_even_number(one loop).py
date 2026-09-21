numbers = [15, 8, 22, 4, 19, 30, 7]

largest = 0

for char in numbers:
    if char % 2 == 0:
        if char > largest:
            largest = char

print(largest)


