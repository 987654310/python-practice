for a in range(1,6):
    d = ""
    for spaces in range(0,5-a):
        d = d + "  "
    for stars in range(0,a):
        d = d + "* "
    print(d)