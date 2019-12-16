"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
https://leetcode.com/problems/n-queens-ii/
"""

from collections import Counter

class Solution(object):
    def totalNQueens0(self, n):
        """
        :type n: int
        :rtype: int
        """

        numThreats = Counter()

        def _isPossibleToPlace(row, col):
            return numThreats[(row, col)] == 0

        
        def _placeQueen(row, col):
            # add row, col, updiag, downdiag
            for i in range(n):
                # add row
                numThreats[(row, i)] += 1
                # add col
                numThreats[(i, col)] += 1
                # add up diag
                upcol = col + row - i
                if upcol >= 0 and upcol < n:
                    numThreats[(i, upcol)] += 1
                # add down diag
                downcol = col - row + i
                if downcol >= 0 and downcol < n:
                    numThreats[(i, downcol)] += 1

        
        def _removeQueen0(row, col):
            # add row, col, updiag, downdiag
            for i in range(n):
                # add row
                numThreats[(row, i)] = max(numThreats[(row, i)] - 1, 0)
                # add col
                numThreats[(i, col)] = max(numThreats[(i, col)] - 1, 0)
                # add up diag
                upcol = col + row - i
                if upcol >= 0 and upcol < n:
                    numThreats[(i, upcol)] = max(numThreats[(i, upcol)] - 1, 0)
                # add down diag
                downcol = col - row + i
                if downcol >= 0 and downcol < n:
                    numThreats[(i, downcol)] = max(numThreats[(i, downcol)] - 1, 0)

            print(numThreats)


        def _removeQueen(row, col):
            # add row, col, updiag, downdiag
            for i in range(n):
                # add row
                numThreats[(row, i)] -= 1
                # if numThreats[(row, i)] < 0:
                #     del numThreats[(row, i)]
                # add col
                numThreats[(i, col)] -= 1
                # add up diag
                upcol = col + row - i
                if upcol >= 0 and upcol < n:
                    numThreats[(i, upcol)] -= 1
                # add down diag
                downcol = col - row + i
                if downcol >= 0 and downcol < n:
                    numThreats[(i, downcol)] -= 1


        def _backtrack(row=0, count=0):
            for col in range(n):
                if _isPossibleToPlace(row, col):
                    _placeQueen(row, col)

                    if row + 1 == n:
                        count += 1
                    else:
                        count = _backtrack(row + 1, count)

                    _removeQueen(row, col)

            return count

        return _backtrack()


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = [1] * n
        upDiag = [1] * (2 * n - 1)
        downDiag = [1] * (2 * n - 1)


        def _isPossibleToPlace(row, col):
            return cols[col] and upDiag[row + col] and downDiag[col - row - n]

        
        def _placeQueen(row, col):
            # add col, updiag, downdiag
            cols[col] = 0
            upDiag[row + col] = 0
            downDiag[col - row - n] = 0

        
        def _removeQueen(row, col):
            # remove col, updiag, downdiag
            cols[col] = 1
            upDiag[row + col] = 1
            downDiag[col - row - n] = 1


        def _backtrack(row=0, count=0, amt=2):
            for col in range(n):
                if row==0:
                    if col > (n-1)//2:
                        return count
                    if n % 2 == 1 and col == (n-1)//2:
                        amt = 1
                    else:
                        amt = 2

                if _isPossibleToPlace(row, col):
                    _placeQueen(row, col)

                    if row + 1 == n:
                        count += amt
                    else:
                        count = _backtrack(row + 1, count, amt)

                    _removeQueen(row, col)

            return count

        return _backtrack()
        

if __name__ == '__main__':
    input = 4
    obj = Solution()
    output = obj.totalNQueens(input)
    print('{} - {}'.format(input, output))