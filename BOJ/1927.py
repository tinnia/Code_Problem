import heapq

n = int(input())
heap = []
answer = []

for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            answer.append(heapq.heappop(heap))
        else:
            answer.append(0)
    else:
        heapq.heappush(heap, data)

for data in answer:
    print(data)