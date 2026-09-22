numbers = [3, 7, 11, 14, 19, 22]

flag = False

for char in numbers:
    if char % 2 == 0 and char > 20:
        flag = True
        print(f"Found {char}")

if flag == False:
    print("Not Found")