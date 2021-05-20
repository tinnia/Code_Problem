class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        square_lst = []
        num = 1
        while num ** 2 <= n:
            square_lst.append(num ** 2)
            num += 1

        answer = 0
        Q = deque()
        Q.append(n)
        while Q:
            answer += 1
            for _ in range(len(Q)):
                x = Q.popleft()
                for sq in square_lst:
                    if sq == x:
                        return answer
                    if sq > x:
                        break
                    Q.append(x - sq)