N, S, M = map(int, input().split())
lst = list(map(int, input().split()))

arr = [[0] * (M + 1) for _ in range(N + 1)]
arr[0][S] = 1

for i in range(1, N + 1):
    for j in range(M + 1):
        if arr[i - 1][j] == 0:
            continue
        if j + lst[i - 1] <= M:
            arr[i][j + lst[i - 1]] = 1
        if j - lst[i - 1] >= 0:
            arr[i][j - lst[i - 1]] = 1

for i in range(M, -1, -1):
    if arr[N][i] == 1:
        print(i)
        break
else:
    print(-1)
