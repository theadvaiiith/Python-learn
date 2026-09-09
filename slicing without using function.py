word = "PythonProgramming"

required = ""
double_increment = 0

while double_increment < len(word):
    required =required + word[double_increment]
    double_increment += 2

print(required)