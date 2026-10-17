numbers = [14, 3, 22, 9, 18, 27, 10]

smallest_odd = None

for num in numbers:
    if num % 2!= 0 and num > 5:
        if smallest_odd is None or num < smallest_odd:
            smallest_odd = num

print(smallest_odd)