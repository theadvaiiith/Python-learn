numbers = [13, 8, 22, 5, 17, 30, 11]

required = None

for num in numbers:
    if (required is None or num > required) and num %2 == 0:
        required = num
print(required)