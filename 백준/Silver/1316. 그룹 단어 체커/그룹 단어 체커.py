n = int(input())
words = []
cnt = 0
for i in range(n):
    words.append(input())

for word in words:
    seen = set()
    is_group = True
    for i in range(len(word)):
        if i>0 and word[i] != word[i-1]:
            if word[i] in seen:
                is_group = False
                break
            seen.add(word[i-1])
    if is_group:
        cnt += 1
print(cnt)