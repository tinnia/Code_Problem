for T in range(1, int(input()) + 1):
    N, A, B = map(int, input().split())

    ans = -1
    for i in range(1, N + 1):
        j = 1
        while i * j <= N:
            func = A * abs(i - j) + B * (N - i * j)
            if ans == -1:
                ans = func
            else:
                ans = min(func, ans)
            j += 1
    print('#{} {}'.format(T, ans))
