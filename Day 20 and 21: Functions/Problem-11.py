def is_prime(num):
    result = True
    for a in range(2,num):
        if num % a == 0:
            result = False
    return result      

for b in range(2,51):
    output = is_prime(b)
    if output == True:
        print(b)