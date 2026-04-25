string = "example"
output = ""

for a in range(0,len(string)):
    if string[a] in "aieou":       
        output = output + "#"
    else:
        output = output + string[a]
print(output)