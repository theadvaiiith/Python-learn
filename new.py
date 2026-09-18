text = "azxxzy"
stack = []

for char in text:
    if stack and stack[-1] == char:
        stack.pop()
    else:
        stack.append(char)
result = "".join(stack)
print(result)