def is_prime(num):
    result = True
    for a in range(2,num):
        if num % a == 0:
            result = False
    return result    

result = is_prime(21)
print(result)


# Dry Run
# num = 21
# a = 2
# a in range True
# 21/2 == 0 False
# a = 3
# a in range True
# 21/3 == 0 True
#
















#    if num <= 1:
#        print("False")
#        return

