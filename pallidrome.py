word = "madam"

reverse = ""

for char in word:
    reverse = char + reverse

if reverse == word:
    print(f"{word} is pallindrome")