arr = [4, 0, 5, 0, 0, 2, 7]


position = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[position], arr[i] = arr[i], arr[position]
        position += 1
print(arr)