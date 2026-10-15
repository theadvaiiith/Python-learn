numbers = [6, 11, 14, 17, 20, 25, 28]

count = 0
total = 0

for num in numbers:
    if (num>10) and (num%2 == 0):
        total+= num
        count+=1

average = total/count
print(f"average is {average}")