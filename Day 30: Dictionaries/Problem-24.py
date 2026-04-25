salaries = {'John': 50000, 'Jane': 60000, 'Doe': 55000}
d = {}

for k,v in salaries.items():
    d[k] = (v/100) * 10 + v
print(d)