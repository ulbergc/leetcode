"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

https://leetcode.com/problems/find-pivot-index/

Solution:
- build cumulative sum from the left and right (L[0] = 0, R[-1] = 0). 
    - If they equal each other, return index
to save time, 
- build from right first
- then build left, checking right as you go
- if match, return

"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        right = [0] * len(nums)
        left = [0] * len(nums)

        # build from the right
        for i in range(len(nums)-1, 0, -1):
            right[i-1] = right[i] + nums[i]

        if right[0] == 0:
            return 0

        # build from the left
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]
            if left[i] == right[i]:
                return i

        return -1
        

if __name__ == '__main__':
    input = [1, 7, 3, 6, 5, 6]
    obj = Solution()
    output = obj.pivotIndex(input)
    print('{} - {}'.format(input, output))