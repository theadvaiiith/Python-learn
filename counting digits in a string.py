word = "PyTh0n123"

digit_count = 0
for char in word:
    if char.isdigit(): #isdigit function used to find the digit count
        digit_count +=1
print(digit_count)