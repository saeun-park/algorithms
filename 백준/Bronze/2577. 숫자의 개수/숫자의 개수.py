a = int(input())
b = int(input())
c = int(input())
m = str(a*b*c)
d = {}

for i in m:
    d[i] = d.get(i, 0)+1

for j in range(10):
    print(d.get(str(j), 0))