numbers = [10, 25, 7, 42, 18]

largest =0 #this works for only positive integers.

"""for negative intergers present in the list use 
largest = numbers[0] #indexing use karo

"""

for char in numbers:
    if char > largest:
        largest = char
print(largest)