def reverse_text(text):

    reverse = ""

    for char in text:
        reverse = char + reverse
    return reverse

print(reverse_text("hello"))  # "olleh"
print(reverse_text("a"))      # "a"
print(reverse_text(""))       # ""
