def func():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for ed, d in street[j]:
                if visit[ed] > visit[j] + d:
                    visit[ed] = visit[j] + d
                    if i == N:
                        print('YES')
                        return
    print("NO")
    return


for TC in range(int(input())):
    N, M, W = map(int, input().split())
    street = [[] for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        street[S].append([E, T])
        street[E].append([S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        street[S].append([E, -T])

    visit = [1e9] * (N + 1)
    func()

