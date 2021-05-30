class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in sorted([(k, v) for k, v in Counter(nums).items()], key=lambda x: x[1], reverse=True)][:k]