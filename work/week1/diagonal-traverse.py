class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        row, col = len(mat), len(mat[0])
        result = []

        for d in range(row + col - 1):
            if d % 2 == 0:
              
                cur_r = min(d, row - 1)
                cur_c = d - cur_r
                while cur_r >= 0 and cur_c < col:
                    result.append(mat[cur_r][cur_c])
                    cur_r -= 1
                    cur_c += 1
            else:
                
                cur_c = min(d, col - 1)
                cur_r = d - cur_c
                while cur_c >= 0 and cur_r < row:
                    result.append(mat[cur_r][cur_c])
                    cur_r += 1
                    cur_c -= 1

        return result