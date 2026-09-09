word = "programming"

count = 0
for char in word:
    if char in ["a","e","i","o","u"]:   #usage of in when checking for in list
        count = count + 1
print(count)