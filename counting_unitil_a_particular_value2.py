numbers = [5, 8, 3, 12, 7, 20]

target_number = 0
total = 0

for char in numbers:
    if char > 10:
        target_number = char
        break


for char in numbers:
    if char == target_number:
        break
    total = total + char
print(total)