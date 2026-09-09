word = "PyTHon"
case_count = 0

for char in word:
    if char.isupper():   #isupper is used to identify the uppercase letters 
        case_count += 1
print(case_count)