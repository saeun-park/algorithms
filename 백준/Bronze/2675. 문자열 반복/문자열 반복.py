n = int(input())
li = []
res = []
for _ in range(n):
    num, w = input().split()
    li.append((int(num), w))

for count, word in li:
    for w in word:
        print(w*count, end="")
    print()
