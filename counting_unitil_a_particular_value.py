numbers = [4, 7, 9, 12, 15, 20]

count = 0
target_number = 0
i = 0
for char in numbers:
    if char > 10 and char % 2 == 0:
        target_number = char
        print(target_number)
        break

for char in numbers:       #indexing the number till the required numebr to fnd the sum.
    if char == target_number:
        break
    count += 1
print(count) 
