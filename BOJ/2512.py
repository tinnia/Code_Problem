N = int(input())
lst = list(map(int, input().split()))
M = int(input())
st, ed = 0, max(lst)
while st <= ed:
    mid = (st + ed) // 2
    ans = 0
    for i in lst:
        ans += min(mid, i)
    if ans > M:
        ed = mid - 1
    else:
        st = mid + 1
print(ed)