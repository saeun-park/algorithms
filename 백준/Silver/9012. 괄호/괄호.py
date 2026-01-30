n = int(input())
li = [input().strip() for _ in range(n)]
    
def is_vps(word):
    stack = []
    for ch in word:
        if ch=='(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack)==0

for l in li:
    if is_vps(l):
        print("YES")
    else:
        print("NO")
            
        
    