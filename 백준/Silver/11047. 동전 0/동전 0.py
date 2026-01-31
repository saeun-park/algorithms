n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = coins[::-1]

cnt = 0
for c in coins:
    if k==0:
        break
    use = k//c
    cnt += use
    k -= use*c
print(cnt)
    