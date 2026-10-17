numbers = [4, 7, 12, 18, 25, 31]
target = 18

flag = False

for num in numbers:
    if num == target:
        flag = True
        break

if flag:
    print("Found")
else:
    print("Not Found")