n = int(input())
res = n
li = []

for i in range(2, int(n**0.5)+1):
    while res%i==0:
        res = res//i
        li.append(i)
    if res==1:
        break
if res>1:
    li.append(res)
for i in li:
    print(i)