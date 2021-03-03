N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))
ans = tmp = 0
for st, ed in lst:
    if st >= tmp:
        ans += 1
        tmp = ed
print(ans)
