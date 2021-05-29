class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        answer = []
        dic = dict(Counter(nums1))
        for num in nums2:
            if num in dic and dic[num]:
                answer.append(num)
                dic[num] -= 1
        return answer