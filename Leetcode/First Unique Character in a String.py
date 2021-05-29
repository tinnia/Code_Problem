class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, v in enumerate(s):
            if v in dic:
                dic[v].append(i)
            else:
                dic[v] = [i]
        idx = 100000
        for k, v in dic.items():
            if len(v) == 1:
                idx = min(idx, v[0])
        if idx == 100000:
            return -1
        else:
            return idx