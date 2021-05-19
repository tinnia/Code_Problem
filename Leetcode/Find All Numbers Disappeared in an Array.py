class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                answer.append(i)
        return answer