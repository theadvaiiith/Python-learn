numbers = [5, 12, 7, 19, 3, 8]
target = 25

found = False

for char in numbers:
    if char == target:
        found = True
        break

if found == False:
    print("Not Found")