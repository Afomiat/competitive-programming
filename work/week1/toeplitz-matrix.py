class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def is_same_diagonal(i, j):
            val = matrix[i][j]
            while i < len(matrix) and j < len(matrix[0]):
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1
            return True

        for i in range(len(matrix)):
            if not is_same_diagonal(i, 0):
                return False

        for j in range(1, len(matrix[0])):
            if not is_same_diagonal(0, j):
                return False

        return True