n = int(input())

for _ in range(n):
    test = input().strip()
    
    score = 0
    streak = 0
    for i in range(len(test)):
        if test[i]=='O':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)
