import math

mi, ma = map(int, input().split())
check = [True]*(ma-mi+1)

for i in range(2, int(math.sqrt(ma))+1):
    sq = i*i
    start = ((mi+sq-1)//sq)*sq
    
    for j in range(start, ma+1, sq):
        check[j-mi] = False
print(sum(check))

