class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        Q = deque()
        Q.append("0000")
        answer = 0
        while Q:
            for x in range(len(Q)):
                x = Q.popleft()
                if x == target:
                    return answer
                for i in range(4):
                    n = int(x[i])
                    for j in (-1, 1):
                        tmp = x[:i] + str((n  + j) % 10) + x[i+1:]
                        if tmp not in deadends:
                            deadends.add(tmp)
                            Q.append(tmp)
            answer += 1
        return -1