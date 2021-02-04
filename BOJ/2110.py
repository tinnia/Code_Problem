N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = sorted(arr)

st = 1
ed = arr[-1] - arr[0]
result = 0

while st <= ed:
    gap = (st + ed) // 2
    tmp = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= tmp + gap:
            tmp = arr[i]
            cnt += 1
    if cnt >= C:
        st = gap + 1
        result = gap
    else:
        ed = gap - 1

print(result)