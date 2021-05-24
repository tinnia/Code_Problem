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

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(ans, nums):
            key = (ans, tuple(nums))
            # cache 에 key 가 있다면,
            if key in cache:
                return cache[key]
            # 모든 nums 원소들을 돌았을 때, ans == target 이면 1 아니면 0 리턴
            if not nums:
                return 1 if ans == target else 0
            # +, - 연산 결과를 합쳐서 res에 담기
            res = dfs(ans - nums[0], nums[1:]) + dfs(ans + nums[0], nums[1:])
            cache[key] = res
            return res

        cache = {}
        return dfs(0, nums)