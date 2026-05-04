class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row.
        # if duplicate, duplicates are checked with a set
        # then, return False
        for row in board:
            duplicates = set()
            for element in row:
                if element in duplicates:
                    return False
                if element != ".":
                    duplicates.add(element)
        
        for i in range(len(board[0])):
            duplicates = set()
            for j in range(len(board)):
                if board[j][i] in duplicates:
                    return False
                if board[j][i] != ".":
                    duplicates.add(board[j][i])
        
        for row in range(0, len(board), 3):
            for col in range(0, len(board), 3):
                duplicates = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] in duplicates:
                            return False
                        if board[i][j] != ".":
                            duplicates.add(board[i][j])
        
        return True



        