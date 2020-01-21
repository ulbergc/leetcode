"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

*** APPROACH ***
Involves backtracking
- backtrack function takes the current position in the word, and the row, col
Start search board for first letter
- Once found, begin second phase
    - Look in adjacent cells for next letter
        - Once one is found, set current to None
            - Makes sure letter isn't repeated
    - Continue until end of word - Success
    - If you don't find next letter, go back to previous position
        - Reset position to its original value
- If you fail with this starting point, continue looking for new starting points

From https://leetcode.com/problems/word-search/
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        L = len(word)
        n = len(board)
        if n == 0:
            return False

        if word == "":
            return True
        
        m = len(board[0])

        def backtrack(index, r, c):
            if index == L - 1:
                return True

            original_val = board[r][c]
            board[r][c] = None

            # Check adjacent nodes
            for d in dirs:
                new_r, new_c = r + d[0], c + d[1]
                if 0 <= new_r < n and 0 <= new_c < m:
                    if board[new_r][new_c] == word[index+1]:
                        if backtrack(index+1, new_r, new_c):
                            return True
                        # else try the next direction

            # At this point, we've failed to find it
            board[r][c] = original_val
            return False


        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == word[0]:
                    if backtrack(0, r, c):
                        return True

        return False
        

if __name__ == '__main__':
    input = ([
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
            ],"Z")
    obj = Solution()
    print(input)
    output = obj.exist(input[0], input[1])
    print('{} - {}'.format(input, output))