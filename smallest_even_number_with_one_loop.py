numbers = [14, 7, 21, 8, 10, 3, 16]

smallest = numbers[0]

for char in numbers:
    if char % 2 ==0:
        if char <= smallest:
            smallest = char
print(smallest)