numbers = [5, 8, 11, 14, 17, 20, 23]

total =0
count =0

for num in numbers:
    if num%2 == 0:
        total += num

    else:
        count += 1

print(total)
print(count)