c = int(input())

for _ in range(c):
    data = list(map(int,input().split()))
    n = data[0]
    scores = data[1:]
    mean = sum(scores)/n
    
    cnt = 0
    for s in scores:
        if s>mean:
            cnt += 1
    print(f"{(cnt*100)/n:.3f}%")
    
    