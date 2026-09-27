def is_palindrome(text):

    text = text.lower()

    reverse = ""

    for char in text:
        reverse = char + reverse

    if reverse == text:
        return True

    else:
        return False

print(is_palindrome("Level"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("a"))      # True
print(is_palindrome(""))       # Trues
