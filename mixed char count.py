word = "Hello123@!"

alpha_count = 0

digit_count = 0

spcl_char_count = 0

for char in word:
    if char.isalpha(): #check if its alphabet 
        alpha_count += 1

    elif char.isdigit():  #checks if its digit
        digit_count += 1

    else:
        spcl_char_count += 1 #else its a spcl char 

print(alpha_count)
print(digit_count)
print(spcl_char_count)