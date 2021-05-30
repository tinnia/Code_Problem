class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        if len(s) < 2:
            return len(s)
        tmp = ""
        for i in s:
            if i not in tmp:
                tmp += i
            else:
                answer = max(answer, len(tmp))
                idx = 0
                while tmp:
                    if tmp[idx] != i:
                        idx += 1
                    else:
                        tmp = tmp[idx + 1:] + i
                        break
        return max(answer, len(tmp))