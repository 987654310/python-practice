string = "Hello world"
output = ""

for a in range(len(string)-1,-1,-1):
    output = output + string[a]
print(output)