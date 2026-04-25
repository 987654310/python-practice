string = "9876543210"
output = ""

for a in range(0,len(string)):
    if a != 6 and a != 7 and a != 8 and a != 9:
        output = output + "*"
    else:
        output = output + string[a]
print(output)
###
#string = 9876543210
#output = ""
#(0,len(string))
#9
#9 != 3,2,1, and 0
#output = output + *
# output = "*"
#8 != 3,2,1, and 0
#output = output + *
# output = "**"
#...
#3 = 3,2,1, and 0 
#output = output + 3
# output = ******3


