def func():
    global flag
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for ed, d in lst[j]:
                if visit[j] != 1e9 and visit[ed] > visit[j] + d:
                    visit[ed] = visit[j] + d
                    if i == N:
                        flag = False
                        return


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    lst[A].append([B, C])

visit = [1e9] * (N + 1)
visit[1] = 0
flag = True
func()
if flag:
    for i in range(2, N + 1):
        if visit[i] == 1e9:
            print(-1)
        else:
            print(visit[i])
else:
    print(-1)