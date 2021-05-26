class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, v in enumerate(nums):
            if i:
                left += nums[i - 1]
            right -= v
            if left == right:
                return i
        return -1