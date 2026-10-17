numbers = [12, 7, 24, 5, 18, 9, 30]

required = None 
even_number = []

for num in numbers:
    if num %2 == 0:
        even_number.append(num)
        even_number.sort()

print(even_number)

for char in even_number:
    if required is None or char < 25:
        required = char

print(required)
