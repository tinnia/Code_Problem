class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        tmp_nums = sorted(list(set(nums)), reverse=True)
        if len(tmp_nums) < 3:
            return tmp_nums[0]
        else:
            return tmp_nums[2]