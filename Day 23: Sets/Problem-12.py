words = {"python", "java", "c++", "ruby", "javascript"}
words_list = list(words)

for a in words_list:#range(1,len(words) + 1):
    if "a" in a:   
        words.remove(a)
print(words)

words.add("swift")

print(words)