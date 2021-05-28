class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        tmp = sum(int(i) ** 2 for i in str(n))
        while 1:
            tmp = sum(int(i) ** 2 for i in str(tmp))
            if tmp == 1:
                return True
            if len(str(tmp)) == 1:
                break
        return False
