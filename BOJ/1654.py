K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
st, ed = 1, max(lst)

while st <= ed:
    mid = (st + ed) // 2
    line = 0
    for i in lst:
        line += i // mid

    if line >= N:
        st = mid + 1
    else:
        ed = mid - 1
print(ed)