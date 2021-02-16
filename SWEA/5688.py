for T in range(1, int(input()) + 1):
    N = int(input())
    ans, i = -1, 0
    while i**3 < N:
        i += 1
        if i ** 3 == N:
            ans = i
            break
    print('#{} {}'.format(T, ans))
