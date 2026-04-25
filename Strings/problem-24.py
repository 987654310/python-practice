s = "hello world python"
a = s.split()
output = ""

for i in range(len(a)):
    output = output + a[i][::-1] + " "
print(output)

#b = a[0][::-1]
#c = a[1][::-1]
#d = a[2][::-1]
#e = b + " " + c + " " + d
#print(e)



