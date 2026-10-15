numbers = [4, 9, 12, 15, 18, 21, 24]

total = 0
count =0 

for num in numbers:
    if (num>10) and (num%3 == 0):
        total = total + num
        count += 1

print(total ,"\n" , count)