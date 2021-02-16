def func(idx, f, k):
    global Max
    if k > L:
        return
    if idx >= N:
        if Max < f:
            Max = f
        return

    func(idx + 1, f + lst[idx][0], k + lst[idx][1])
    func(idx + 1, f, k)


for T in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    Max = 0
    func(0, 0, 0)
    print('#{} {}'.format(T, Max))
