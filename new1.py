arr = [2, 2, 1, 2, 3, 2, 2]

freq = {}

for char in arr:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

new_list = [int(char) for char in freq]
print(new_list)

largest = 0
for i in new_list:
    if i > largest:
        largest = i
print(largest)

