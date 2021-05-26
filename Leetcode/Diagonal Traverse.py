class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        n, m = len(mat), len(mat[0])
        result = []
        for i in range(n + m - 1):
            stack = []
            if i < m:
                r, c = 0, i
            else:
                r, c = i - m + 1, m - 1

            while r < n and c > -1:
                stack.append(mat[r][c])
                r += 1
                c -= 1

            if i % 2:
                result.extend(stack)
            else:
                result.extend(stack[::-1])
        return result