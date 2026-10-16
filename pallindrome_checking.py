def is_palindrome(text):

    is_pallindrome = True

    reverse = ""

    for char in text:
        reverse = char + reverse

    if reverse == text:
        return is_pallindrome
    else:
        return not is_pallindrome


print(is_palindrome("madam"))



