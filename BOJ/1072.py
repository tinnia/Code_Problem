X, Y = map(int, input().split())
Z = Y / X * 100
if Z >= 99:
    print(-1)
else:
    st, ed, ans = 0, X, -1
    while st <= ed:
        mid = (st + ed) // 2
        nx, ny = X + mid, Y + mid
        if (ny / nx * 100) > Z:
            ans = mid
            ed = mid - 1
        else:
            st = mid + 1
    print(ans)
