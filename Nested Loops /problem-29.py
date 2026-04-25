for a in range(1,6):
    d = ""
    for b in range(1,a):
        d = d + " "
    for c in range(1,7-a):
        d = d + "*"  
    print(d)

for e in range(1,6):
    h = ""
    for f in range(1, 5-e+1):
        h = h + " "
    for g in range(1,e+1):
        h = h + "*"     
    print(h)


# e = 1
# h = ""
# 5 - 1 + 1 = 5
# 4
# h = h + " "
# "    "
# 1 + 1 = 2
# 1
# "*"    