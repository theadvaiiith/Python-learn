

def is_palindrome(text):

    text = text.lower()
    reverse = ""

    for letter in text:
        reverse = letter + reverse

    return text == reverse

print(is_palindrome("Madam"))



