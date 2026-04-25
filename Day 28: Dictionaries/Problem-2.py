#a = input("Enter country name: ")

countries = ["India", "France", "Japan", "Canada"]
capitals = ["New Delhi", "Paris", "Tokyo", "Ottawa"]

d = {}
for a in range(0,len(countries)):
    d[countries[a]] = capitals[a]

print(d)

# for b,c in d.items():
#     if a in b:
#         print(c)
