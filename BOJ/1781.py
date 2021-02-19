import heapq

N = int(input())
lst = []
for i in range(N):
    x, y = map(int, input().split())
    heapq.heappush(lst, (x, y))

answer = []
for i in lst:
    heapq.heappush(answer, i[1])
    if i[0] < len(answer):
        heapq.heappop(answer)

print(sum(answer))
