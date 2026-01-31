s = input().strip()
n = len(s)
li = []

for i in range(n):
    for j in range(i, n):
        li.append(s[i:j+1])
print(len(set(li)))
        
    