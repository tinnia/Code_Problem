# Time Limit
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         self.cnt = 0
#
#         def dfs(depth, ans):
#             if depth == len(nums):
#                 if ans == target:
#                     self.cnt += 1
#                 return
#             for i in [-1, 1]:
#                 dfs(depth + 1, ans + i * nums[depth])
#
#         dfs(0, 0)
#         return self.cnt
