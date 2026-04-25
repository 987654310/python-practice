#    1 2 3 4 5
# 1  * * * * *
# 2  *       *
# 3  *       *
# 4  * * * * *


for a in range(1,5):
    c = ""
    if a==1 or a==4:
        for b in range(1,6):
            c = c + "* "
    else:
        for b in range(1,6):
            if b==1 or b==4:
                c = c + "* "
            else:
                c = c + "   "
    print(c)