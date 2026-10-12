"""if a number is either:
- between 1 and 10 inclusive
  or
- divisible by 7"""

def check(num):
    if 1<= num <= 10 or num%7 == 0:
        print("accepted")
    else:
        print("rejected")

check(21)