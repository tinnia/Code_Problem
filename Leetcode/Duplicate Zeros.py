class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """ Do not return anything, modify arr in-place instead. """
        answer = []
        for item in arr:
            if len(answer) == len(arr):
                break
            if not item:
                answer.append(item)
                answer.append(item)
        for i in range(len(arr)):
            arr[i] = answer[i]