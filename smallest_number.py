numbers = [14, 7, 25, 9, 31, 18]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)
