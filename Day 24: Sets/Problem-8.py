letters = {"a", "b", "c", "d", "e"}

letter_list = list(letters)

for a in letter_list:
    if a in "aeiou":
        letters.remove(a)

print(letters)