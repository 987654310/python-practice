#string = ["Data", "Science", "Python"]
#output = ",".join(string)
#print(output)


words = ["Data", "Science", "Python"]
output1 = ""

for a in range(0,len(words)):
    output1 = output1 + words[a] 
    if a != len(words) - 1:    
        output1 = output1 + ","
print(output1)


