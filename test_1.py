def check_pass(num):
    if (num >= 20 and num <= 100) and num%4 == 0:
        print("qualified")

    else:
        print("not qualified")

check_pass(44)