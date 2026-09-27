def count_vowels(text):

    list = ["a", "e", "i", "o", "u"]
    
    text = text.lower()

    count = 0

    for char in text:
        if char in list:
            count += 1

    return count

print(count_vowels("hello"))     # 2
print(count_vowels("AEIOU"))     # 5
print(count_vowels("Python"))    # 1
print(count_vowels(""))          # 0