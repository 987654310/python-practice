for f in range(1, 6):
    b = ""
    for spaces in range(0, 5-f):
        b = b + " "
    
    for star in range(0, 2*f-1):
        b = b + "*"
    
    print(b)
