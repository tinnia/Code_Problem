for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = [i for i in range(1, N+1) if i not in lst]
    print('#{}'.format(T), end=' ')
    print(*ans)