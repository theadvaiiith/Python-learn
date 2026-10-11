def intro_elif(number):

    if number > 0:
        print(f"number {number} positive")

    elif number < 0:
        print(f"number {number} negative")

    else:
        print(f"number {number} zero")

intro_elif(-7)