"""num > 0 and even   → "Positive Even"
num > 0 and odd    → "Positive Odd"
num < 0            → "Negative"
num == 0           → "Zero"""

def odd_even(num):
    if num ==0:
        print("zero")
    elif num >0 and num%2 == 0:
        print("even")
    elif num>0 and num%2 != 0:
        print("odd")
    else:
        print("negative")

odd_even(17)