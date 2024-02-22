class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

       
        count = 0

        row = [max(row) for row in grid]
        col = [max(col) for col in zip(*grid)]
        r = len(row)
        c = len(col)
        min_val = [[0] * r for _ in range(c)]
        
        for i in range(r):
            for j in range(c):
                min_val[i][j] = min(row[i], col[j])
        
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    count += abs(grid[i][j] - min_val[i][j])
                

        return count