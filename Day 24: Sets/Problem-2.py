s = set()
num = {1,2,3}

s.update(num)

if 2 in s:
    s.discard(2)

print(s) 
