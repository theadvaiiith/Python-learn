number = int(input("Enter a number: "))

reverse = 0

while number>0:
    digit = number%10
    reverse = reverse*10 + digit
    number = number//10
print(reverse)

if number == reverse:
    print(f"{number} is a palindrome")

else:
    print(f"{number} is not a palidrome")
