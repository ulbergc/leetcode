"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
https://leetcode.com/problems/plus-one/
"""

class Solution(object):
    # ITERATIVE
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1

        while True:
            if i == -1:
                digits = [1] + digits
                break
            elif digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                i -= 1

        return digits


    # RECURSIVE
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        def _addOneToInd(digits, i):
            if i == -1:
                digits = [1] + digits
                return digits
            elif digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                return _addOneToInd(digits, i-1)

        return _addOneToInd(digits, n-1)

if __name__ == '__main__':
    input = [1,2,3]
    oginput = input[:]
    obj = Solution()
    output = obj.plusOne(input)
    print('{} - {}'.format(oginput, output))