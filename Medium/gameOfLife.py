"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
https://leetcode.com/problems/game-of-life/

"""

class Solution(object):
    def gameOfLife0(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        changes = []
        m = len(board)
        n = len(board[0])

        def _countNeighbors(i, j):
            # get NW, N, NE, W, E, SW, S, SE
            total = 0
            if i > 0:
                # N 
                total += board[i-1][j]
                if j > 0:
                    # NW 
                    total += board[i-1][j-1]
                if j < n-1:
                    # NE 
                    total += board[i-1][j+1]
            if j > 0:
                # W 
                total += board[i][j-1]
            if j < n-1:
                # E 
                total += board[i][j+1]
            if i < m-1:
                # S
                total += board[i+1][j]
                if j > 0:
                    # SW 
                    total += board[i+1][j-1]
                if j < n-1:
                    # SE 
                    total += board[i+1][j+1]

            return total

        for i in range(m):
            for j in range(n):
                count = _countNeighbors(i, j)

                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        changes.append((i, j, 0))
                else:
                    if count == 3:
                        changes.append((i, j, 1))

        for change in changes:
            board[change[0]][change[1]] = change[2]
                
                
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        changes = []
        m = len(board)
        n = len(board[0])

        for i in range(m):
            check = [0]
            if i > 0:
                check.append(-1)
            if i < m-1:
                check.append(1)
            R = sum(board[i+x][0] for x in check)
            C = 0
            prev = 0
            
            for j in range(n):
                cur = board[i][j]
                L = C + prev
                C = R - cur
                R = sum(board[i+x][j+1] for x in check) if j < n-1 else 0

                count = L + C + R
                prev = cur

                if cur == 1:
                    if count < 2 or count > 3:
                        changes.append((i, j, 0))
                else:
                    if count == 3:
                        changes.append((i, j, 1))

        for change in changes:
            board[change[0]][change[1]] = change[2]
        

if __name__ == '__main__':
    # input = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    input = [[]]
    obj = Solution()
    output = obj.gameOfLife(input)
    print('{} - {}'.format(input, output))