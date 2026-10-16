def reverse_word_order(sentence):
    words = sentence.split(" ")
    print(words)

    reverse = ""
    for char in words:
        reverse = char + " " + reverse

    return reverse.rstrip()

print(reverse_word_order("Use a loop for practice"))


def reverse_word_order(sentence):
    words = sentence.split(" ")
    print(words)

    reverse = ""
    for char in words:
        reverse = char + " " + reverse

    return reverse

print(reverse_word_order("Use a loop for practice"))




