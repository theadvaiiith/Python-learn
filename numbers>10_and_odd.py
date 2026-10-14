numbers = [3, 8, 11, 14, 17, 20, 25]

count = 0

for num in numbers:
    if num>10 and num%2 != 0:
        count+= 1

print(count)