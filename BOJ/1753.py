import sys
import heapq

input = sys.stdin.readline


def func(st):
    visit[st] = 0
    heap = []
    heapq.heappush(heap, (0, st))
    while heap:
        d, now = heapq.heappop(heap)
        if visit[now] < d:
            continue
        for i, j in graph[now]:
            j += d
            if visit[i] > j:
                visit[i] = j
                heapq.heappush(heap, (j, i))


V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    x, y, w = map(int, input().split())
    graph[x].append([y, w])

visit = [3000001] * (V + 1)
func(K)
for i in range(1, V + 1):
    if visit[i] == 3000001:
        print('INF')
    else:
        print(visit[i])
