for T in range(1, int(input()) + 1):
    A, B, C = map(int, input().split())
    if A < B:
        print('#{} {}'.format(T, C // A))
    else:
        print('#{} {}'.format(T, C // B))
