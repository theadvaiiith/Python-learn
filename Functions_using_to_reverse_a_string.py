def count_vowels(text):

    reverse = ""

    for char in text:
        reverse = char + reverse
    return reverse

print(count_vowels("hello"))     # 2
print(count_vowels("AEIOU"))     # 5
print(count_vowels("Python"))    # 1
