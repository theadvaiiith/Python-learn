arr = [2, 2, 1, 2, 3, 2, 2]

freq = {}

for char in arr:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

new_list = freq.list