


def cleaned_string(text):
    cleaned = ""
    text = text.lower()
    for letter in text:
        if letter.isalnum():
            cleaned = cleaned + letter

    return cleaned

def is_pllindrome(text):
    word = cleaned_string(text)

    reverse = ""
    for char in word:
        reverse = char + reverse

    if reverse == word:
        return True


print(is_pllindrome("A man, a plan, a canal: Panama"))