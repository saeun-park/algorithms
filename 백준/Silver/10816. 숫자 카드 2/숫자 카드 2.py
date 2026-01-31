from collections import Counter
n = int(input())
sangeun = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))

count = Counter(sangeun)
ans = [count[c] for c in card]

print(*ans)
