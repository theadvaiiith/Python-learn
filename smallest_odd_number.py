numbers = [14, 9, 25, 7, 18, 11, 30]

required = None

for num in numbers:
    if (required is None or num < required) and num %2 != 0:
        required = num 

print(required)