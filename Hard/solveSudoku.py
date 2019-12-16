"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
https://leetcode.com/problems/sudoku-solver/
"""

class Solution(object):
    def solveSudoku0(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        v_count = 0 
        b_count = 0

        def is_valid(num, row, col):
            nonlocal v_count
            v_count += 1
            box_i = row - row % 3
            box_j = col - col % 3
            for i in range(9):
                if board[i][col] == num:
                    return False
                if board[row][i] == num:
                    return False
                if board[box_i + i // 3][box_j + i % 3] == num:
                    return False
                
            return True


        def find_next_pos(row=0):
            for i in range(row, 9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i, j

            # this should never happen
            return False


        def backtrack(row, rem):
            nonlocal b_count
            b_count += 1
            if rem == 0:
                return True

            row, col = find_next_pos(row)
            # try each number
            for num in '123456789':
                if is_valid(num, row, col):
                    # place number
                    board[row][col] = num

                    # backtrack(spot[0], spot[1], rem - 1)
                    if backtrack(row, rem - 1):
                        return True
                    else:
                        # if backtrack returns False, remove number (='.')
                        board[row][col] = '.'

            return False
                    
        numBlank = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    numBlank += 1

        backtrack(0, numBlank)
        print('is_valid calls: {}'.format(v_count))
        print('backtrack calls: {}'.format(b_count))


    def solveSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        v_count = 0 
        b_count = 0

        rows, cols, boxes = [], [], []
        for _ in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())

        # rows = [set()] * 9
        # cols = [set()] * 9
        # boxes = [set()] * 9

        def is_valid(num, row, col):
            nonlocal v_count
            v_count += 1
            if num in rows[row] or num in cols[col] or num in boxes[_box_num(row, col)]:
                return False
                
            return True


        def _box_num(row, col):
            return (row // 3) * 3 + col // 3


        def place_number(num, row, col):
            board[row][col] = num
            rows[row].add(num)
            cols[col].add(num)
            boxes[_box_num(row, col)].add(num)


        def remove_number(num, row, col):
            board[row][col] = '.'
            rows[row].remove(num)
            cols[col].remove(num)
            boxes[_box_num(row, col)].remove(num)


        def find_next_pos(row=0):
            for i in range(row, 9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i, j

            # this should never happen
            return False


        def backtrack(row, rem):
            nonlocal b_count
            b_count += 1
            if rem == 0:
                return True

            row, col = find_next_pos(row)
            # try each number
            for num in '123456789':
                if is_valid(num, row, col):
                    # place number
                    place_number(num, row, col)

                    # backtrack(spot[0], spot[1], rem - 1)
                    if backtrack(row, rem - 1):
                        return True
                    else:
                        # if backtrack returns False, remove number (='.')
                        remove_number(num, row, col)

            return False
                    
        numBlank = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    numBlank += 1
                else:
                    place_number(board[i][j], i, j)

        print(numBlank)
        print('rows')
        print(rows)
        print('cols')
        print(cols)
        print('boxes')
        print(boxes)
        backtrack(0, numBlank)
        print('is_valid calls: {}'.format(v_count))
        print('backtrack calls: {}'.format(b_count))


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        v_count = 0 
        b_count = 0

        rows, cols, boxes = [], [], []
        for _ in range(9):
            rows.append([0]*9)
            cols.append([0]*9)
            boxes.append([0]*9)

        # rows = [set()] * 9
        # cols = [set()] * 9
        # boxes = [set()] * 9

        def is_valid(num, row, col):
            nonlocal v_count
            v_count += 1
            i = int(num) - 1
            if rows[row][i] or cols[col][i] or boxes[_box_num(row, col)][i]:
                return False
                
            return True


        def _box_num(row, col):
            return (row // 3) * 3 + col // 3


        def place_number(num, row, col):
            board[row][col] = num
            i = int(num) - 1
            rows[row][i] = 1
            cols[col][i] = 1
            boxes[_box_num(row, col)][i] = 1


        def remove_number(num, row, col):
            board[row][col] = '.'
            i = int(num) - 1
            rows[row][i] = 0
            cols[col][i] = 0
            boxes[_box_num(row, col)][i] = 0


        def find_next_pos(row=0):
            for i in range(row, 9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i, j

            # this should never happen
            return False


        def backtrack(row, rem):
            nonlocal b_count
            b_count += 1
            if rem == 0:
                return True

            row, col = find_next_pos(row)
            # try each number
            for num in '123456789':
                if is_valid(num, row, col):
                    # place number
                    place_number(num, row, col)

                    # backtrack(spot[0], spot[1], rem - 1)
                    if backtrack(row, rem - 1):
                        return True
                    else:
                        # if backtrack returns False, remove number (='.')
                        remove_number(num, row, col)

            return False
                    
        numBlank = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    numBlank += 1
                else:
                    place_number(board[i][j], i, j)

        print(numBlank)
        print('rows')
        print(rows)
        print('cols')
        print(cols)
        print('boxes')
        print(boxes)
        backtrack(0, numBlank)
        print('is_valid calls: {}'.format(v_count))
        print('backtrack calls: {}'.format(b_count))


    def printBoard(self, board):
        for i, row in enumerate(board):
            if i % 3 == 0:
                print('_____________')
            row_str = ''
            for j, col in enumerate(row):
                if j % 3 == 0:
                    row_str += '|' 
                row_str += col
            print(row_str + '|')
        print('_____________')


if __name__ == '__main__':
    input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    obj = Solution()
    print('Board')
    obj.printBoard(input)
    output = obj.solveSudoku(input)
    # print('{} - {}'.format(input, output))
    print('Board')
    obj.printBoard(input)