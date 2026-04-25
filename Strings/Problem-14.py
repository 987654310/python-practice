string = "Python is an amazing language"
words = string.split()
max = 0

for a in words:
    if len(a) > max:
        max = len(a)
        longest_word = a
print(longest_word)