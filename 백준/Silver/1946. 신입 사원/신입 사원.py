import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    li = []
    for _ in range(n):
        x, y = map(int, input().split())
        li.append((x, y))
    
    li.sort(key=lambda x: x[0])
    a = li[0][1]
    cnt = n
    for i in range(1, n):
        if li[i][1] <=a:
            a = li[i][1]
        else:
            cnt -= 1
            
    print(cnt)