word = "hello"

reverse = ""

for char in word:
    reverse = char + reverse

if reverse == word:
    print(f"{reverse} is a palindrome")
else:
    print(f"{reverse} is not a palindrome")