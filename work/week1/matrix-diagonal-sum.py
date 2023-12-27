class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        result = 0
        # dia = {}
        # rev_dia = {}
        if l == 1:
            return mat[0][0]
        else:
            for i in range(l):
                for j in range(l):
                    if i - j == 0:
                        result += mat[i][j]
                    elif i + j == l - 1:
                        result += mat[i][j]

        return result