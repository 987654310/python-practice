fruits = set()
fruit_list = list(fruits)

a = {"apple", "banana", "cherry"} 

fruits.update(a)

if "banana" in a:
    a.remove("banana")

print(a) 
