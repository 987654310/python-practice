sentence = ["hello", "world", "hello"]

count1 = 0
count2 = 0

for a in range(0,len(sentence)):
    if "hello" in sentence[a]:
        count1 = count1 + 1

for a in range(0,len(sentence)):
    if "world" in sentence[a]:
        count2 = count2 + 1



d = {
"hello": count1,
"world": count2
}
print(d)