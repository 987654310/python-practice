string = "HeLLo WoRLD"
output = ""

for a in string:
    if a.isupper():
        output = output + a.lower() 
    elif a.islower():
        output = output + a.upper()
    else:
        output = output + " "
print(output)