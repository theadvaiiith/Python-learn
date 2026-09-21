numbers = [15, 8, 22, 4, 19, 30, 7]
largest = 0
even_number = []

for char in numbers:
    if char % 2 == 0:
       even_number.append(char)

for new in even_number:
    if new > largest:
        largest = new
print(largest)


