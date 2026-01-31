n = int(input())
arr = [input().strip() for _ in range(n)]
deque = []

for a in arr:
    if a=='size':
        print(len(deque))
    elif a=='empty':
        print(1 if not deque else 0)
    elif a=='front':
        print(deque[0] if deque else -1)
    elif a=='back':
        print(deque[-1] if deque else -1)
        
    elif a.split()[0]=='push_front':
        i = int(a.split()[1])
        deque.insert(0, i)
    elif a.split()[0]=='push_back':
        i = int(a.split()[1])
        deque.append(i)
    elif a.split()[0]=='pop_front':
        if deque:
            print(deque[0])
            deque.pop(0)
        else: print(-1)
    elif a.split()[0]=='pop_back':
        if deque:
            print(deque[-1])
            deque.pop()
        else: print(-1)