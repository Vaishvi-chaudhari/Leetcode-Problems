class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        live_neighbors += board[x][y] & 1 

                if board[i][j] == 1: 
                    if live_neighbors == 2 or live_neighbors == 3:
                        board[i][j] |= 2
                else: 
                    if live_neighbors == 3:
                        board[i][j] |= 2 

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1