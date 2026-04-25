s = "example"
def replaceAllVowelsWithLowercase(str):
    output = ""
    #s = "example"
    for a in range(0,len(s)):
        if s[a] in "aeiou":
            output = output + "#"
        else:
            output = output + s[a]
    print(output)

replaceAllVowelsWithLowercase(s)

