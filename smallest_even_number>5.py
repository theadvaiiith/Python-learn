numbers = [8, 3, 15, 6, 21, 10, 18]

required = None

for num in numbers:
    if num > 5:
        if (required is None or num < required) and num %2 == 0:
            required = num

print(required)
