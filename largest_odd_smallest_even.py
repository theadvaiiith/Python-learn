numbers = [11, 28, 7, 34, 19, 42, 5]

largest_odd = None

smallest_even = None

for num in numbers:
    if num%2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

    else:
        if smallest_even is None or num < smallest_even:
            smallest_even = num

print(largest_odd)
print(smallest_even)