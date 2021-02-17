import heapq


def dijkstra(start):
    heap_data = [(start, 0)]
    distance = [1e9] * (n + 1)
    distance[start] = 0
    while heap_data:
        com, dis = heapq.heappop(heap_data)
        if distance[com] >= dis:
            for i, j in arr[com]:
                j += dis
                if distance[i] > j:
                    distance[i] = j
                    heapq.heappush(heap_data, (i, j))

    answer = [0, 0]
    for i in distance:
        if i != 1e9:
            answer[0] += 1
            answer[1] = max(i, answer[1])

    print(*answer)


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append((a, s))

    dijkstra(c)
