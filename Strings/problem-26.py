s = input("Input: ")
reversed_str = ""

splitting = s.split()
removing_spaces = "".join(splitting)
l = removing_spaces.lower()

reversed_str = l[::-1]
#or for a in range(len(l)-1,-1,-1):
#    reversed_str = reversed_str + l[a]

if reversed_str == l:
    print("True")
else: 
    print("False")
