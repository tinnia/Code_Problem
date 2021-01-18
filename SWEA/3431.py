for T in range(1, int(input())+1):
    L, U, X = map(int,input().split())
    res = 0
    if X < L:
        res = L - X
    elif X > U:
        res = -1

    print('#{} {}'.format(T, res))