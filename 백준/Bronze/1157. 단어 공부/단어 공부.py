word = input().strip()
word = word.lower()

cnt = {}
for w in word:
    cnt[w] = cnt.get(w, 0)+1

max_values = []
max_cnt = max(cnt.values())

for i in cnt:
    if cnt[i]==max_cnt:
        max_values.append(i)

if len(max_values)>1:
    print("?")
else:
    print(max_values[0].upper())