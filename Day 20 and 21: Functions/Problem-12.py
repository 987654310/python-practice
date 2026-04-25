def reverse_string(s):
    output = ""
    for a in range(len(s)-1,-1,-1):
        output = output + s[a]
    return output

output = reverse_string("hello")
print(output)