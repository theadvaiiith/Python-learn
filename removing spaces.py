word = "hello world python"
word1 = "hello world python"

result = ""
result1 = ""

for char in word:
    if char.isalpha():
        result = result + char
print(result)

# another way for any input
for char in word1:
    if char != " ":
        result1 = result1 + char
print(result1)