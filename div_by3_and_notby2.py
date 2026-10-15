numbers = [6, 9, 12, 15, 18, 21, 24]

total =0
count=0

for num in numbers:
    if (num%3 == 0) and (num%2 != 0):
        total += num
        count += 1

average = total/count
print(average)
