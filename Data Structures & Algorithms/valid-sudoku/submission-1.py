from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        sub = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] in row[i]:
                    return False
                elif board[i][j] in column[j]:
                    return False
                elif board[i][j] in sub[(i//3),(j//3)]:
                    return False
                elif board[i][j] != ".":
                    row[i].add(board[i][j])
                    column[j].add(board[i][j])
                    sub[(i//3,j//3)].add(board[i][j])
        
        return True



                
        
        