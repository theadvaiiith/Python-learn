text = "10 20 30 40"

new_list = text.split(" ")

numbers = [int(num) for num in new_list] #list comprehension
print(numbers)
