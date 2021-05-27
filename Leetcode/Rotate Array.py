class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k == 0:
            return nums
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:- k]
        return nums