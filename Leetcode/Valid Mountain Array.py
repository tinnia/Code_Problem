class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        flag = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            elif not flag and arr[i] > arr[i + 1]:
                if i == 0:
                    return False
                else:
                    flag = 1
            elif flag and arr[i] < arr[i + 1]:
                return False
        if flag:
            return True
        else:
            return False