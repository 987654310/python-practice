for a in range(1, 6):
    d = ""
    for b in range(0, 5-a):
        d = d + " "
    for c in range(0, 2*a-1):
        a = str(a)
        d = d + a
    print(d)

