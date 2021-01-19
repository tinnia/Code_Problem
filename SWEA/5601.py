for T in range(1, int(input())+1):
    N = int(input())
    print('#{}'.format(T), end=' ')
    for _ in range(N):
        print('1/{}'.format(N), end=' ')
    print()