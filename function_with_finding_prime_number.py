
def is_prime(n):
    is_prime = True

    if n <= 1:
        is_prime = False

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("True")

    else:
        print("False")

    


is_prime(0)   # False
is_prime(1)   # False
is_prime(2)   # True
is_prime(9)   # False
is_prime(13)  # True