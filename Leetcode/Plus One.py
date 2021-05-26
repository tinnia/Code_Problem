class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        tmp = int(''.join(digits)) + 1
        return list(str(tmp))