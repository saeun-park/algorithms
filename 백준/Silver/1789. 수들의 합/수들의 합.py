s = int(input())
prev_s = 0
n = 0

while prev_s+n+1 <=s:
    n += 1
    prev_s += n
    
print(n)