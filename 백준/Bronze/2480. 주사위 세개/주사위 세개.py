li = list(map(int, input().split()))
uniq = set(li)

if len(uniq)==1:
    print(10000+li[0]*1000)
elif len(uniq)==2:
    for x in uniq:
        if li.count(x)==2:
            print(1000+x*100)
else:
    print(max(li)*100)