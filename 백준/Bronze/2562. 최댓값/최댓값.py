li = [0]*9

for i in range(9):
    li[i] = int(input())
   
for j in range(9):
    if li[j]==max(li):
        print(li[j])
        print(j+1)

