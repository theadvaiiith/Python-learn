def reverse_string(text):
    reverse = ""

    for char in text:
        reverse = char + reverse 

    return reverse



def reverse_each_word(sentence):
    words = sentence.split()
    reversed_string = []

    for word in words:
        reversed_word = reverse_string(word)
        reversed_string.append(reversed_word)

    return " ".join(reversed_string)

print(reverse_each_word("Hello Buddy"))
