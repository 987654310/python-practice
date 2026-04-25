string = "education"
count = 0

for a in range(0,len(string)):
    if string[a] in "aieou":       
        count = count + 1
print(f"The word education has {count} vowels")


