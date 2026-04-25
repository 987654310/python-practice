from datetime import datetime

now = datetime.now()
print(now)
print("------------------------")

d = {
    "a" : 1,
    "b": 2
}

for k, v in d.items():
    now_s = str(now)
    d[k] = now_s
print(d)
print("------------------------")

l = []

l.append(now)
print(l)