for T in range(1, int(input()) + 1):
    D, A, B, F = map(int, input().split())
    p = D / (A + B)
    print('#{} {:.6f}'.format(T, p*F))