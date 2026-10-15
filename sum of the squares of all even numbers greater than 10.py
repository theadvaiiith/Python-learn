numbers = [4, 7, 10, 13, 16, 19, 22]

total =0

for num in numbers:
    if num > 10 and num%2 == 0:
        total += (num**2)

print(total)