def special(num):
    if num <0 or (num%3 == 0 and num%5 == 0):
        print("special")

    else:
        print("normal")

special(30)