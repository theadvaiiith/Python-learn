numbers = [18, 5, 12, 3, 9, 1, 7]

smallest = None 
second_smallest = None 

for num in numbers:
    if smallest is None or num < smallest:
        second_smallest = smallest
        smallest = num

    elif (second_smallest is None or num < second_smallest) and num > smallest:
        second_smallest = num
print(smallest)
print(second_smallest)