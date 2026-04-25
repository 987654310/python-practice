words = ["apple", "banana", "kiwi", "mango", "grape"]
count = 0

for a in range(0,len(words)):
    if len(words[a]) == 5:
        count = count + 1
print(count)