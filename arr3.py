arr = [10, 5, 8, 10, 3]

largest = arr[0]
second_largest = arr[1]

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i

    elif largest > i > second_largest:
        second_largest = i
        
print(second_largest)