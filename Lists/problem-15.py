#final_num = 0
#list = [1,2,3,2,1]
#final_list = []
#list2 = []


#for a in range(0,len(list)+1):
#    r = a%10
#    final_num = final_num * 10 + r
#    a = a//10
#if a == final_num:
#    print("True")
#else:
#    print("False")
#print(a)







list = [1,2,3,2,5]
reversed_list = list[::-1]
if reversed_list == list:
    print("True")
else:
    print("False")

# Python List Notes
# K[ : : ] ⇒ start from the very beginning, go up to the last element, and include every element (imp)
# Rule➖ By default slicing work from left to right (imp)
# K=[ 1, 2, 3, "Sam", "Danny", True, 3.4, [ 1, 4, 5, 6, 7 ] ]
#print(K[-4][::-1])     # => ynnaD