class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = collections.defaultdict(int)
        for i in nums1:
            for j in nums2:
                dic[i + j] += 1

        answer = 0
        for i in nums3:
            for j in nums4:
                if (-i - j) in dic:
                    answer += dic[(-i - j)]
        return answer
