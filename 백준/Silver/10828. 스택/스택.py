n = int(input())
li = [input().strip() for _ in range(n)]
stack = []

for i in li:
    if "push" in i:
        n = i.split()[1]
        stack.append(n)
    elif i=="top":
        print(-1 if not stack else stack[-1])
    elif i=="size":
        print(len(stack))
    elif i=="empty":
        print(1 if not stack else 0)
    elif i=="pop":
        if not stack: 
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

        

    
        