n = int(input())

for _ in range(n):
    test = input().strip()
    
    score = 0
    pos = 0
    for i in range(len(test)):
        if test[i]=='O':
            pos += 1
            score += pos
        else:
            pos = 0
    print(score)
