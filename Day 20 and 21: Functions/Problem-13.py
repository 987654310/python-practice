def is_palindrome(s):
    output = ""
    palindrome = False
    for a in range(len(s)-1,-1,-1):
        output = output + s[a]
    if s == output:
        palindrome = True
    return palindrome
        
palindrome = is_palindrome("hello")
print(palindrome)