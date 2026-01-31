n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [float('inf')]*(k+1)
dp[0] = 0

for c in coin:
    for x in range(c, k+1):
        dp[x] = min(dp[x], dp[x-c]+1)

print(dp[-1] if dp[-1] != float('inf') else -1)
    