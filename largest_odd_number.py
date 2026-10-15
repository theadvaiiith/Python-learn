numbers = [12, 5, 18, 7, 25, 9, 30]


required = None

for num in numbers:
    if (required is None or num > required) and num%2 != 0:
        required = num 

print(required)