class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        def checkDistance(mat, i, j):
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            Q = collections.deque([(i, j, 0)])
            while Q:
                r, c, di = Q.popleft()
                for x in range(4):
                    nr, nc = r + d[x][0], c + d[x][1]
                    if 0 <= nr < m and 0 <= nc < n:
                        if mat[nr][nc] == 0:
                            mat[i][j] = di + 1
                            return
                        Q.append((nr, nc, di + 1))

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    checkDistance(mat, i, j)
        return mat