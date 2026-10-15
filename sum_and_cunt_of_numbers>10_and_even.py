numbers = [5, 8, 12, 15, 20, 23, 30]

total = 0
count = 0

for num in numbers:
    if (num > 10) and (num%2 == 0):
        total += num
        count+=1

print(f"total sum {total}")
print(f"count of numbers {count}")