N, S = map(int, input().split())
lst = list(map(int, input().split()))
st, ed = 0, 1
ans, tmp = N + 1, sum(lst[0:2])
while st <= ed:
    if tmp < S:
        ed += 1
        if ed >= N:
            break
        tmp += lst[ed]
    else:
        ans = min(ans, ed - st + 1)
        tmp -= lst[st]
        st += 1
if ans == N + 1:
    print(0)
else:
    print(ans)