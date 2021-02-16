for T in range(1, int(input()) + 1):
    N = int(input())
    lst = [0] * 501
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A-1, B):
            lst[i] += 1
    ans = []
    p = int(input())
    for i in range(p):
        c = int(input())
        ans.append(lst[c-1])
    print('#{}'.format(T), end=' ')
    print(*ans)