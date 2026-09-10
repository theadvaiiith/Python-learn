text = "10 20 30 40 50"


new_text = text.split(" ")

int_list = [int(num) for num in new_text] #list comprhension
print(int_list)
print(type(int_list))

total = 0

for i in int_list:               #running through a for loop ot find the total
    total = total + i
print(total)