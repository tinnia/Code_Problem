for T in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    lst = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            lst[j] = i
    print('#{}'.format(T), end=' ')
    print(*lst)