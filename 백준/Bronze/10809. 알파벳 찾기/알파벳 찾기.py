word = input().strip()
res = [-1]*26

for i in range(len(word)):
    idx = ord(word[i])-ord('a')
    if res[idx] == -1:
        res[idx] = i

print(*res)

