n, s = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
c = 0
ans = n+1

while True:
    if c>=s:
        ans = min(ans, right-left)
        c -= nums[left]
        left += 1
    elif right==n:
        break
    else:
        c += nums[right]
        right += 1

print(ans if ans != n+1 else 0)