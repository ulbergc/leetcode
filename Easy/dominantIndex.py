"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.
https://leetcode.com/problems/largest-number-at-least-twice-of-others/
"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dom, sec, ind0 = -1, -1, -1

        for i, n in enumerate(nums):
            if n > dom:
                sec = dom
                dom = n
                ind0 = i
            elif n > sec:
                sec = n

        if dom >= sec * 2:
            return ind0
        else:
            return -1
        

if __name__ == '__main__':
    input = [1, 2, 3, 4]
    input = [3, 6, 1, 0]
    obj = Solution()
    output = obj.dominantIndex(input)
    print('{} - {}'.format(input, output))