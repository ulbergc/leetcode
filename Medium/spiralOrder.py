"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
https://leetcode.com/problems/spiral-matrix/

Keep track of current position, direction, and bounds
Continue in same direction until reaching a boundary, then turn right (and change that boundary)
- turn right (URDL) 
    - dirs = [(-1, 0), (1, 0), (1, 0), (0, -1)]
    - dir = (dir + 1) % 4

"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # dirs = up, right, down, left
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        heading = 1 # right
        i, j = 0, 0

        # bounds
        # u, r, d, l = 0, len(matrix[0]), len(matrix), -1
        bounds = [-1, len(matrix[0]), len(matrix), -1]

        spiral = []
        # while u < d and l < r:
        for _ in range(len(matrix) * len(matrix[0])):
            spiral.append(matrix[i][j])
            new_i = i + dirs[heading][0]
            new_j = j + dirs[heading][1]
            # if boundary is hit, change boundary and turn
            if (new_i == bounds[0] or new_i == bounds[2] 
                or new_j == bounds[1] or new_j == bounds[3]):
                b_ind = (heading - 1) % 4
                bounds[b_ind] += -sum(dirs[b_ind])
                heading = (heading + 1) % 4
                new_i = i + dirs[heading][0]
                new_j = j + dirs[heading][1]

            i, j = new_i, new_j

        return spiral
        

if __name__ == '__main__':
    # input = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    input = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    obj = Solution()
    output = obj.spiralOrder(input)
    print('{} - {}'.format(input, output))