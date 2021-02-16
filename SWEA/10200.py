for T in range(1, int(input()) + 1):
    N, A, B = map(int, input().split())
    if A + B <= N:
        print('#{} {} {}'.format(T, min(A, B), 0))
    else:
        print('#{} {} {}'.format(T, min(A, B), (A + B) - N))
