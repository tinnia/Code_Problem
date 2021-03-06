import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    visit[0][0] = 1
    while heap:
        cnt, r, c = heapq.heappop(heap)
        if r == N - 1 and c == M - 1:
            print(cnt)
            return
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc <M and visit[nr][nc] == 0:
                visit[nr][nc] = 1
                if arr[nr][nc] == "1":
                    heapq.heappush(heap, (cnt + 1, nr, nc))
                else:
                    heapq.heappush(heap, (cnt, nr, nc))


M, N = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
bfs()
