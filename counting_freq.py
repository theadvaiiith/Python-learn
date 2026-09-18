arr = [4, 1, 4, 2, 1, 4, 3]

freq = {}

for value in arr:
    if value in freq:
        freq[value] += 1
    else:
        freq[value] = 1
print(freq)