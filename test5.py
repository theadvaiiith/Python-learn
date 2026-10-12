"""only if a number:
- is greater than 50
- is even
- is not divisible by 5"""

def check_valid(num):
    if num>50 and num%2 ==0 and num%5 != 0:
        print("valid")

    else:
        print("invalid")

check_valid(64)