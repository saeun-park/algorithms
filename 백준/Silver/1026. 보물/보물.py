n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sort_a = sorted(a)
sort_b = sorted(b)[::-1]

res = 0
for i in range(n):
    res += sort_a[i]*sort_b[i]
    
print(res)