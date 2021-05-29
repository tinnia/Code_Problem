class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        for idx, val in enumerate(list1):
            dic[val] = [idx]
        for idx, val in enumerate(list2):
            if val in dic:
                dic[val].append(idx)
        cnt, ans = 2000, []
        for i, v in dic.items():
            if len(v) == 2:
                if cnt > sum(v):
                    cnt = sum(v)
                    ans = [i]
                elif cnt == sum(v):
                    ans.append(i)
        return ans