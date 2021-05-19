class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                idx = max(idx, i)
                while idx < len(nums):
                    if nums[idx] != 0:
                        nums[i] = nums[idx]
                        nums[idx] = 0
                        break
                    idx += 1

        return nums