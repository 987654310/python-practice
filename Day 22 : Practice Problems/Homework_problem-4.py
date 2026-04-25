def function(units, commercial):
    original = units[:]
    cost = []
    sum = 0
    revenue = 0

    for a in range(0,len(units)):
        if original[a] >= 0 and original[a] <= 100:
            b = (units[a] * 3) + 50
            cost.append(b)
        elif original[a] >= 101 and original[a] <= 300:
            c = (units[a] * 5) + 50
            cost.append(c)
        elif original[a] >= 301 and original[a] <= 500:
            d = (units[a] * 7) + 50
            cost.append(d)
        elif original[a] > 500:
            e = (units[a] * 10) + 50
            cost.append(e)

    for a in range(0,len(units)):
        sum = sum + units[a] 
        if sum < 1000:
            cost[a] = cost[a] - ((cost[a]/100) * 5)

    for a in range(len(commercial)):
        if commercial[a] == True:
            cost[a] = cost[a] + ((cost[a]/100) * 20)

    for a in range(0,len(units)):
        revenue = revenue + cost[a]
    return cost, revenue

cost, revenue = function([120, 450, 600, 80], [False, True, False, False])
print(f"Bills: {cost}, Total Revenue: {revenue}")







###########



###########

# def function(units, commercial):
#     original = units
#     cost = []

#     for a in range(0,len(units)):
#         if original[a] >= 0 and original[a] <= 100:
#             units[a] = (units[a] * 3) + 50

#         elif original[a] >= 101 and original[a] <= 300:
#             units[a] = (units[a] * 5) + 50
    
#         elif original[a] >= 301 and original[a] <= 500:
#             units[a] = (units[a] * 7) + 50

#         elif original[a] > 500:
#             units[a] = (units[a] * 10) + 50

#     print(units)
#     print(original)


# function([120, 450, 600, 80], [False, True, False, False])