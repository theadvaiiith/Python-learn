numbers = [3, 9, 12, 15, 22, 27, 30]

total = 0
count = 0

for num in numbers:
    if num%3 == 0:
        total += num 
    if num > 20:
        count += 1

print(total)
print(count)
