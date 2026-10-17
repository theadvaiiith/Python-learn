

def count_characters(text):

    count_storage = {}

    for char in text:
        if char in count_storage:
            count_storage[char] += 1

        else:
            count_storage[char] = 1



    return count_storage 

print(count_characters("banana"))