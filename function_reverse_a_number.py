def reverse_number(n):

    if n == 0:
        return 0


    reverse = 0
    digit = 0

    while n > 0:
        digit = n % 10
        reverse = reverse*10 + digit

        n = n // 10

    return reverse

print(reverse_number(507))  # 705
print(reverse_number(120))  # 21
print(reverse_number(0))    # 0
