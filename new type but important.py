def clean_text(text):

    words = text.lower()

    new_text = ""
    for letter in words:
        if letter.isalnum():
            new_text = new_text + letter

    return new_text

print(clean_text("Hi, Buddy! 123"))