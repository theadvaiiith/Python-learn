numbers = [18, 7, 25, 4, 11, 2]

smallest = None 
second_smallest = None 


for char in numbers:
    if smallest is None or char < smallest:
        second_smallest = smallest
        smallest = char

    elif char > smallest and (second_smallest is None or char < second_smallest):
        second_smallest = char

print(smallest)
print(second_smallest)