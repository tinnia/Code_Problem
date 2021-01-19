for _ in range(10):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    Max = 0
    for c in range(100):
        tmp = tmp1 = 0
        for r in range(100):
            tmp += arr[r][c]
            tmp1 += arr[c][r]
        Max = max(tmp, Max, tmp1)

    tmp = tmp1 = 0
    for r in range(100):
        tmp += arr[r][r]
        tmp1 += arr[r][-1-r]
    Max = max(tmp, tmp1, Max)

    print('#{} {}'.format(T, Max))