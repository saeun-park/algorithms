k, n = map(int, input().split())
lanes = [int(input()) for _ in range(k)]

low, high = 1, max(lanes)
ans = 0

while low <= high:
    mid = (low+high)//2
    cnt = 0
    for l in lanes:
        cnt += l//mid
    if cnt >=n:
        ans = mid
        low = mid+1
    else:
        high = mid-1
print(ans)
        
        
