string = input("Enter a word: ")
unique_character = ""
count = 0

for a in range(0,len(string)):
    character = string[a]
    count = 0
    for b in range(0,len(string)):
        if string[b] == character:
            count = count + 1
    if count == 1:
        print(character)
        break
    



        
        

