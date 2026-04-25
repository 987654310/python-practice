words = {"hello", "world", "python", "programming", "sets"}
words_list = list(words)

for a in words_list:
    if len(a) > 5:
        words.remove(a)
words.add("code")

print(words)