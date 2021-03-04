N, M = map(int, input().split())
tree = list(map(int, input().split()))
st, ed = 1, max(tree)

while st <= ed:
    mid = (st + ed) // 2
    ans = 0
    for i in tree:
        if i >= mid:
            ans += i - mid
    if ans >= M:
        st = mid + 1
    else:
        ed = mid - 1
print(ed)