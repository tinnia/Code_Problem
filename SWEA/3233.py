for T in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    print('#{} {}'.format(T, (A // B) ** 2))
