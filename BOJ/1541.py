lst = input().split('-')
ans = 0
for i in lst[0].split('+'):
    ans += int(i)
for i in lst[1:]:
    for j in i.split('+'):
        ans -= int(j)
print(ans)