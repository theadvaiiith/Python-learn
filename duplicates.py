

def duplicate_check(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return num
        else:
            seen.add(num)

    return None

print(duplicate_check([5, 3, 8, 3, 5]))

