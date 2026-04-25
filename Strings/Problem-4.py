string =  "python"
output = ""
b = ""
b = b + string[0]
c = ""
c = c + string[len(string) - 1]

for a in range(1,len(string) -1):
    output = output + string[a]      
output = c + output + b    
print(output)