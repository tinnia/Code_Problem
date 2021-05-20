class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            Q = deque()
            Q.append((r, c))
            while Q:
                x, y = Q.popleft()
                for i in range(4):
                    nx = x + d[i][0]
                    ny = y + d[i][1]
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        Q.append((nx, ny))

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    cnt += 1
        return cnt