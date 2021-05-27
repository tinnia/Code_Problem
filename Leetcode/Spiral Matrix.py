class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        answer = []

        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur = i = j = 0
        for _ in range(n * m):
            answer.append(matrix[i][j])
            matrix[i][j] = ""
            ni, nj = i + d[cur][0], j + d[cur][1]
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] != "":
                i, j = ni, nj
            else:
                cur = (cur + 1) % 4
                i, j = i + d[cur][0], j + d[cur][1]
        return answer