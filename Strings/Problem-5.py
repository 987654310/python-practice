string = "hello"
output = ""
middle = len(string)//2

for a in range(0,len(string)):
    if a == middle:
        output = output + string[a].upper()
    else:
        output = output + string[a]
print(output)
