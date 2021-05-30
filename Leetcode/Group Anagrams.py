class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        for st in strs:
            answer[tuple(sorted(st))].append(st)
        return answer.values()