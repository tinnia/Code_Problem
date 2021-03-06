import heapq


def func(k):
    visit = [1e9] * (N + 1)
    visit[k] = 1
    heap = []
    heapq.heappush(heap, (0, k))
    while heap:
        t, x = heapq.heappop(heap)
        for b, time in lst[x]:
            tmp = t + time
            if visit[b] > tmp:
                visit[b] = tmp
                heapq.heappush(heap, (tmp, b))
    return visit


N, M, X = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    lst[a].append([b, t])

ans = [0] * (N + 1)
for i in range(1, N + 1):
    arr1 = func(i)
    ans[i] += arr1[X]
    arr2 = func(X)
    ans[i] += arr2[i]
print(max(ans))