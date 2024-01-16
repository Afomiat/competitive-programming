class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.prifix = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                self.prifix[i + 1][j + 1] = self.prifix[i][j + 1] + self.prifix[i + 1][j] - self.prifix[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prifix[row2 + 1][col2 + 1] - self.prifix[row1][col2 + 1] - self.prifix[row2 + 1][col1] + self.prifix[row1][col1]
        return result