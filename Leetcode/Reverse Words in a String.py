class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i for i in s.split() if i != ""]
        s[:] = s[::-1]
        return ' '.join(s)