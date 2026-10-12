numbers = [5, 12, 18, 7, 24, 31, 40]

count = 0

for num in numbers:
    if num%2 ==0 and num>15:
        count += 1
print(count)