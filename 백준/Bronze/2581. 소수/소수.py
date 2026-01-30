m = int(input())
n = int(input())

def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i ==0:
            return False
    return True

s = 0
p = []
for i in range(m, n+1):
    if is_prime(i):
        s += i
        p.append(i)
if p:
    print(s)
    print(min(p))
else:
    print(-1)