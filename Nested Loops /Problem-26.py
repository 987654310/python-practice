#       1 2 3 4 5
#  1        *
#  2        *
#  3    * * * * *
#  4        *
#  5        *

for rows in range(1,6):
    c = ""
    for columns in range(1,6):
        if rows == 3 or columns == 3:    
            c = c + "* "
        else:
            c = c + "  "
    print(c)    