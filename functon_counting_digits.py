def count_digits(n):

    if n == 0:
        return 1

    count = 0

    while n > 0:
        count += 1
        n = n // 10
    return count

print(count_digits(507))  # 3
count_digits(8)    # 1
count_digits(0)    # 1






