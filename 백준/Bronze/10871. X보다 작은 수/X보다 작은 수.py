a, x = map(int,input().split())
nums = list(map(int, input().split()))
res = []

for num in nums:
    if num < x:
        res.append(num)
print(*res)