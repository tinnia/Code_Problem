class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                del dic[num]
            else:
                dic[num] = 1
        for k in dic.keys():
            return k