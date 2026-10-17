

def find_duplicates(numbers):
    seen = set()

    duplicates = []

    for num in numbers:
        if num in seen:
            if num not in duplicates:   
                duplicates.append(num)

        else:
            seen.add(num)

    return duplicates


print(find_duplicates([5, 3, 8, 3, 5, 3]))