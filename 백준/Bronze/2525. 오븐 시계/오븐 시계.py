h, m = map(int, input().split())
p = int(input())

print((h + (m+p)//60)%24, (m+p)%60)