n = int(input())
for _ in range(n):
    num, word = input().split()
    print("".join(w*int(num) for w in word))
