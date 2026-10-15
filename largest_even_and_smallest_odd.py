numbers = [14, 3, 22, 8, 19, 27, 10]

required_even = None

required_odd = None

for num in numbers:

    if num %2 ==0:
        if (required_even is None) or (num > required_even):
            required_even = num

    else:
        if (required_odd is None) or (num < required_odd):
            required_odd = num

print(required_even)
print(required_odd)