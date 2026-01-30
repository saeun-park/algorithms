word = input().strip()
parts = word.split('-')

left = sum(map(int, parts[0].split('+')))
right = 0
for p in parts[1:]:
    right += sum(map(int, p.split('+')))

print(left-right)

