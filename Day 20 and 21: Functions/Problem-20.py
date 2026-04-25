def remove_duplicates(l):
    output = []
    for a in range(0,len(l)): 
        element = l[a] 
        
        if element not in output:
            output.append(element)  
    return output

output = remove_duplicates([1, 2, 2, 3, 4, 4, 5, 5])
print(output)
#Dry Run
#output = []
# for a in range(0,len(l))
#True
#a = 0
#element = 1
#output = [1]
#a = 1
# element = 2
#output = [1,2]
# 
