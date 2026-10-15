numbers = [14, 7, 25, 9, 31, 18]


largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)