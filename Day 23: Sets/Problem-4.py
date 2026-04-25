colors = {"red", "green", "blue"}

colors.remove("yellow")

print(colors)

#Gives an error because element doesn't exsist in set


#


colors = {"red", "green", "blue"}

colors.discard("yellow")

print(colors)

# Doesn't give an error even though element doesn't exsist