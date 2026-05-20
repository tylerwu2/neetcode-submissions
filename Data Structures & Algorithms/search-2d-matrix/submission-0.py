class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mid = len(matrix) // 2
        if target < matrix[mid][0]:
            mid = mid - 1
            for i in range(0, mid+1):
                for j in range(len(matrix[mid])):
                    if target == matrix[i][j]:
                        return True
        else:
            for i in range(mid, len(matrix)):
                for j in range(len(matrix[mid])):
                    if target == matrix[i][j]:
                        return True
        return False 