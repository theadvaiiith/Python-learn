text = "10 20 30 40 50"

new_text = text.split(" ")

int_list = [int(char) for char in new_text]
print(int_list)

total = 0

for char in int_list:
    total = total + char


count = len(int_list) #if list is full of integers then use len to find length
print(count)

average = total/count
print(average)