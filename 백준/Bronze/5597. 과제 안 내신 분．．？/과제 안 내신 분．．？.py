li = []
for _ in range(28):
    li.append(int(input()))

all_student = set(range(1, 31))
t = set(li)
f = all_student-t

print(min(f))
print(max(f))