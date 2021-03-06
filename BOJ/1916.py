import heapq


def func(st):
    visit[st] = 1
    heap = []
    heapq.heappush(heap, (0, st))
    while heap:
        cash, idx = heapq.heappop(heap)
        if visit[idx] < cash:
            continue
        for i, j in lst[idx]:
            tmp = cash + j
            if visit[i] > tmp:
                visit[i] = tmp
                heapq.heappush(heap, (cash + j, i))


N = int(input())
M = int(input())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y, w = map(int, input().split())
    lst[x].append([y, w])
st, ed = map(int, input().split())
visit = [1e9] * (N + 1)
func(st)
print(visit[ed])