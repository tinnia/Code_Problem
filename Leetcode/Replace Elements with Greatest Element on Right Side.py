class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1
        else:
            pointer = 0
            for i in range(len(arr)):
                if i == pointer:
                    pointer = i + 1
                    for j in range(i + 2, len(arr)):
                        if arr[pointer] < arr[j]:
                            pointer = j
                if i == pointer or pointer == len(arr):
                    arr[i] = -1
                else:
                    arr[i] = arr[pointer]
        return arr