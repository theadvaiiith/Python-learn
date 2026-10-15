numbers = [3, 6, 9, 12, 15, 18]

count = 0 
total = 0

for num in numbers:
    if num%6 == 0:
        total = num + total
        count+= 1

average = total/count
print(average)