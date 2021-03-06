import heapq


def func(k):
    visit = [1e9] * (N + 1)
    visit[k] = 0
    heap = []
    heapq.heappush(heap, (0, k))
    while heap:
        time, a = heapq.heappop(heap)
        for b, t in lst[a]:
            tmp = t + time
            if visit[b] > tmp:
                visit[b] = tmp
                heapq.heappush(heap, (tmp, b))
    return visit


N, E = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    lst[a].append([b, c])
    lst[b].append([a, c])
v1, v2 = map(int, input().split())
st = func(1)
mid = func(v1)
ed = func(v2)
ans = min(st[v1] + mid[v2] + ed[N], st[v2] + ed[v1] + mid[N])
if ans >= 1e9:
    print(-1)
else:
    print(ans)
