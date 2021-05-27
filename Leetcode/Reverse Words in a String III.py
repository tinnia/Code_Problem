class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i[::-1] for i in s.split()]
        return " ".join(s)