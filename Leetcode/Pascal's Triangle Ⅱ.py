class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [[1] * i for i in range(1, 35)]
        if rowIndex < 2:
            return arr[rowIndex]
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        return arr[rowIndex]