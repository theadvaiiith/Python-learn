numbers = [12, 7, 18, 5, 20, 9, 14, 3]

count =0 

for char in numbers:
    if char % 2 == 0 and char > 10:
        count +=1
print(count)