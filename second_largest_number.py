numbers = [10, 25, 7, 42, 18]

largest = numbers[0]
second_largest = 0

for char in numbers:
    if char > largest:
        second_largest = largest
        largest = char
    elif largest > char > second_largest:
        second_largest = char
print(largest)
print(f"second_largest: {second_largest}")