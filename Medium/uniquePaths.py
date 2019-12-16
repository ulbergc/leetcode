"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
https://leetcode.com/problems/unique-paths/
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        arr = [[None] * (n-1) for _ in range(m-1)]

        # arr[0][0] = 1
        for i in range(m-1):
            for j in range(n-1):
                up = 1 if i-1 < 0 else arr[i-1][j]
                left = 1 if j-1 < 0 else arr[i][j-1]
                arr[i][j] = up + left
                # if not arr[i][j]:
                #     arr[i][j] = up + left
                # up = 0 if i-1 < 0 else arr[i-1][j]
                # left = 0 if j-1 < 0 else arr[i][j-1]
                # if not arr[i][j]:
                #     arr[i][j] = up + left

        return arr[m-2][n-2]

        
if __name__ == '__main__':
    input = (7,3)
    obj = Solution()
    output = obj.uniquePaths(input[0], input[1])
    print('{}: {}'.format(input, output))