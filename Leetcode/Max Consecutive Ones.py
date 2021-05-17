class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = cnt = 0
        for num in nums:
            if num:
                cnt += 1
            else:
                cnt = 0
            answer = max(answer, cnt)
        return answer