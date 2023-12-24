class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
   
        dict_col = {}
        dict_row = {}
        
        for i in range(9):
            for j in range(9):
                if board[i][j] not in ['1','2','3','4','5','6','7','8','9','.']:
                    return False

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] not in dict_row:
                    dict_row[board[i][j]] = 1
                elif board[i][j] != '.' and board[i][j] in dict_row:
                    return False
                   
            dict_row = {}

        col_wise = list(zip(*board))
        for i in range(9):
            for j in range(9):
                if col_wise[i][j] not in ['1','2','3','4','5','6','7','8','9','.']:
                    return False
                    
        for i in range(9):
            for j in range(9):
                if col_wise[i][j] != '.' and col_wise[i][j] not in dict_col:
                    dict_col[col_wise[i][j]] = 1
                elif col_wise[i][j] != '.' and col_wise[i][j] in dict_col:
                    return False
                    
            dict_col = {}
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                my_set = set()
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        if board[row][col] != '.':
                            if board[row][col] in my_set:
                                return False
                            my_set.add(board[row][col])

        return True
     
