class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = sum([nums[i] for i in range(len(nums)) if i % 2 == 0])
        return ans