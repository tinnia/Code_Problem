for _ in range(1, 11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    Max = 0

    # 가로
    for i in range(100):
        for j in range(99):
            if arr[i][j] == arr[i][j + 1]:
                cnt, n = 2, 1
                while j - n >= 0 and j + n < 99:
                    if arr[i][j - n] == arr[i][j + n + 1]:
                        cnt += 2
                        n += 1
                    else: break
                Max = max(Max, cnt)
            else:
                cnt = n = 1
                while j - n >= 0 and j + n < 100:
                    if arr[i][j - n] == arr[i][j + n]:
                        cnt += 2
                        n += 1
                    else: break
                Max = max(Max, cnt)

    # 세로
    for i in range(99):
        for j in range(100):
            if arr[i][j] == arr[i + 1][j]:
                cnt, n = 2, 1
                while i - n >= 0 and i + n < 99:
                    if arr[i - n][j] == arr[i + n + 1][j]:
                        cnt += 2
                        n += 1
                    else: break
                Max = max(Max, cnt)
            else:
                cnt = n = 1
                while i - n >= 0 and i + n < 100:
                    if arr[i - n][j] == arr[i + n][j]:
                        cnt += 2
                        n += 1
                    else: break
                Max = max(Max, cnt)

    print('#{} {}'.format(T, Max))
