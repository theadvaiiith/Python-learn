word = "HackerRank123"

count = 0

for char in word:
    if char.islower() == True:
        count += 1
print(count)