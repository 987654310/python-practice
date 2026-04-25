def factorial(num):
    s = 1
    f = 1
    while (s <= num): 
        f = s * f
        s = s + 1
    return f
f = factorial(5)
print(f)
