#  1 2 3 4  5
# 1*       *
# 2 *   *
# 3   *



for rows in range(1,4):
    c = ""
    for columns in range(1,6):
        if rows == 3 or columns == 3:    
            c = c + "* "
        else:
            c = c + "  "
    print(c) 
#####
for f in range(1, 6):
    b = ""
    for spaces in range(0, 5-f):
        b = b + " "
    
    for star in range(0, 2*f-1):
        b = b + "*"
    
    print(b)