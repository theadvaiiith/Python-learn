numbers = [11, 17, 23, 28, 31]

found = False

for char in numbers:
    if char % 2 == 0:
        found = True
        print("Even number found")
        break

if found == False:
    print("Even number not found")
