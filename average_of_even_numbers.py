numbers = [4, 7, 10, 13, 16, 19]

total =0 
count =0

average = 0

for num in numbers:
    if num%2 == 0:
        total = total + num
        count+=1

    average = total / count

print(average)

    