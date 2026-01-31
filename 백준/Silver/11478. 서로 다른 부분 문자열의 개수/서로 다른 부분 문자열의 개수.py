s = input().strip()
n = len(s)
li = []

for i in range(n):
    pos = i
    while pos<=n-1:
        li.append(s[i:pos+1])
        pos += 1
print(len(set(li)))
        
    