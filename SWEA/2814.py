def func(i, cnt):
    global ans
    if ans < cnt:
        ans = cnt
    for idx in lst[i]:
        if not visit[idx]:
            visit[idx] = 1
            func(idx, cnt + 1)
            visit[idx] = 0

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    if M == 0:
        print('#{} 1'.format(T))
    else:
        ans = 0
        visit = [0] * (N+1)
        lst = [[] for _ in range(N+1)]

        for _ in range(M):
            n, m = map(int, input().split())
            lst[n].append(m)
            lst[m].append(n)

        for i in range(1, N+1):
            visit[i] = 1
            func(i, 1)
            visit[i] = 0

        print('#{} {}'.format(T, ans))