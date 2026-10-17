numbers = [10, 40, 20, 50, 30]

largest = None 
second_largest = None 

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num

    elif (second_largest is None or num >second_largest) and num < largest:
        second_largest = num

print(largest)
print(second_largest)