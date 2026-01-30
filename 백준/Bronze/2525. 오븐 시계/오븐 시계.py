h, m = map(int, input().split())
p = int(input())

total_min = m+p

if total_min<60:
    print(h, total_min)
else:
    new_h = (h+total_min//60)%24
    new_m = (total_min)%60
    print(new_h, new_m)
    