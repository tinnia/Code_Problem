N, M = map(int, input().split())
lst = list(map(int, input().split()))

st = ed = ans = 0
while st <= ed <= len(lst):
    S = sum(lst[st:ed])
    if S == M:
        ans += 1
    if S <= M:
        ed += 1
    elif M < S and st < ed:
        st += 1
    else:
        st += 1
        ed += 1
print(ans)