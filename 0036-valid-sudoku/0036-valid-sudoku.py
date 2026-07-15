class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in board: # Check rows
            seen = set()
            for num in row:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)

        for col in range(9): # Check columns
            seen = set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        for row in range(0, 9, 3): # Check 3x3 boxes
            for col in range(0, 9, 3):
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] != ".":
                            if board[r][c] in seen:
                                return False
                            seen.add(board[r][c])
        return True