class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
      
        for g_row, g_col in guards:
            grid[g_row][g_col] = 2
        for w_row, w_col in walls:
            grid[w_row][w_col] = 2
      
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
      
        for g_row, g_col in guards:
            for delta_row, delta_col in directions:
                row, col = g_row, g_col
                while 0 <= row + delta_row < m and 0 <= col + delta_col < n and grid[row + delta_row][col + delta_col] < 2:
                    row, col = row + delta_row, col + delta_col
                    grid[row][col] = 1
                  
        return sum(cell == 0 for row in grid for cell in row)