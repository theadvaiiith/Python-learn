numbers = [10, 25, 7, 42, 18]

smallest = numbers[0]

for char in numbers:
    if char <= smallest:
        smallest = char
print(smallest)