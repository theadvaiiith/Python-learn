numbers = [2, 4, 7, 10, 13, 16, 19]

total =0
count =0

for num in numbers:
    if num%2 == 0:
        total += num

    else:
        count+= 1

print(f"sum of even {total}")
print(f"count of odd {count}")