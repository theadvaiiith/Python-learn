word = "PyThOn123@Code"

count = 0

for char in word:
    if char.isupper() == True or char.isdigit() == True:
        count += 1
print(count)