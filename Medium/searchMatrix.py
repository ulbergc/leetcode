"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def _subSearch(r0, r1, c0, c1, level):
            if r1 < r0 or c1 < c0:
                return False
            if r0 == r1 and c0 == c1:
                return matrix[r0][c0] == target
            mid_r = (r0 + r1) // 2
            mid_c = (c0 + c1) // 2

            if matrix[mid_r][mid_c] < target:
                return (_subSearch(r0, mid_r, mid_c + 1, c1, level + 1) 
                    or _subSearch(mid_r + 1, r1, c0, mid_c, level + 1)
                    or _subSearch(mid_r + 1, r1, mid_c + 1, c1, level + 1))
            elif matrix[mid_r][mid_c] > target:
                return (_subSearch(mid_r, r1, c0, mid_c - 1, level + 1) 
                    or _subSearch(r0, mid_r - 1, mid_c, c1, level + 1)
                    or _subSearch(r0, mid_r - 1, c0, mid_c - 1, level + 1))
            else:
                return True


        return _subSearch(0, len(matrix) - 1, 0, len(matrix[0]) - 1, 0)


if __name__ == '__main__':
    input = ([
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ], 0)
    obj = Solution()
    output = obj.searchMatrix(input[0], input[1])
    print('{} - {}'.format(input, output))