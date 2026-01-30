n = int(input())
grade = list(map(int, input().split()))
new_grade = []
m = max(grade)

for g in grade:
    new_grade.append(g/m*100)
    
print(sum(new_grade)/n)