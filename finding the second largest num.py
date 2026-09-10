numbers = [10, 25, 7, 42, 18]

largest = numbers[0]
second_largest = numbers[1]

for char in numbers:
    if char > largest:
        second_largest = largest
        largest = char
print(second_largest)

