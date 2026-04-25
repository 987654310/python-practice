def functions(items):
    original = items
    s = 0
    d = 0

    for a in range(0,len(items)):                          
        if original[a] >= 100 and original[a] <= 499: 
            items[a] = items[a] - (items[a]/100) * 10
        #or 
        #for a in range(0,len(items)):
        #d = (items[a]/100) * 10
        #if original[a] >= 100 and original[a] <= 499: 
        #   items[a] = items[a] - d   

        if original[a] >= 500 and original[a] <= 999: 
            items[a] = items[a] - (items[a]/100) * 20
        
        if original[a] >= 1000:
            items[a] = items[a] - (items[a]/100) * 25
    
    print(items)
    
    original_2 = s
    for a in range(0,len(items)):
        s = s + items[a] 

    if original_2 > 2000:
        s = s - (s/100) * 5


    if len(items) >= 5:
       s = s - 100
    
    return items, s
    
items, s = functions([150, 80, 750, 1200, 300])
print(f"Items: {items}, Final Total: {s}")