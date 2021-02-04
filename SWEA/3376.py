for T in range(1, int(input()) + 1):
    N = int(input())
    p = [0] * 101
    p[0] = p[1] = p[2] = 1
    for i in range(3, N):
        p[i] = p[i - 2] + p[i - 3]

    print('#{} {}'.format(T, p[N - 1]))
