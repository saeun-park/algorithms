word = input().strip()
frula = input().strip()
new = []

for w in word:
    new.append(w)
    if len(new)>=len(frula) and "".join(new[-len(frula):]) == frula:
        del new[-len(frula):]
print("".join(new) if new else "FRULA")