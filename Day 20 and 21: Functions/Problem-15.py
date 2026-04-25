def maximum(num):
    max = num[0]
    for a in num:
        if a > max:
            max = a  
    return  max

max = maximum([10, 20, 15])
print(max)


#def maximum(num):
#    max = num[0]
#    #if num[0] > num[1] and num[2]:
#    #    print(num[0])
#    #    return
#    if num[1] > num[2] and num[0]:
#        max = num[1]
#    if num[2] > num[0] and num[1]:
#        max = num[2]
#    return max
#max = maximum([10,15,20])
#print(max)