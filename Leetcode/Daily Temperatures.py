class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                tmp = stack.pop()
                answer[tmp] = idx - tmp
            stack.append(idx)
        return answer
