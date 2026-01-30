li = list(map(int, input().split()))
m = {}

for i in li:
    m[i] = m.get(i, 0)+1

if len(m)==1:
    print(10000+li[0]*1000)
elif len(m)==2:
    for key, val in m.items():
        if val==2:
            print(1000+key*100)
else:
    print(max(li)*100)
    
