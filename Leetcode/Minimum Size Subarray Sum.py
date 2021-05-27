class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j, tmp, ans = 0, 0, len(nums) + 1
        for i in range(len(nums)):
            tmp += nums[i]
            while tmp >= target:
                ans = min((i - j + 1), ans)
                tmp -= nums[j]
                j += 1
        return ans if ans != len(nums) + 1 else 0
