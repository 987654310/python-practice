string = "abc123xyz456"
count = 0

for a in range(0,len(string)):
    if string[a].isnumeric(): 
        count = count + 1
print(count)