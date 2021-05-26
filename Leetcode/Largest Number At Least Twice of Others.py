class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        Max = nums.index(max(nums))
        for i in range(len(nums)):
            if i == Max:
                continue
            if nums[i] * 2 > nums[Max]:
                return -1
        return Max