class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx, length = 0, len(nums) - 1
        while idx < length:
            if nums[idx] == nums[idx+1]:
                nums.remove(nums[idx+1])
                length -= 1
            else:
                idx += 1
        return len(nums)