class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = dict()
        dic2 = dict()
        for i in range(len(s)):
            if s[i] in dic1:
                if t[i] != dic1[s[i]]:
                    return False
            else:
                if t[i] in dic2:
                    return False
                else:
                    dic1[s[i]] = t[i]
                    dic2[t[i]] = ""
        return True