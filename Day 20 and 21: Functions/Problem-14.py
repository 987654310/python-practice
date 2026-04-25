def count_vowels(s):
    count = 0
    for a in s:
        if a in "aeiou":
            count = count + 1
        elif a in "AEIOU":
            count = count + 1
    return count

count = count_vowels("Hello")
print(count)