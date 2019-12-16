"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
https://leetcode.com/problems/missing-number/
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n)
        n = len(nums)
        mask = n

        for i, num in enumerate(nums):
            mask ^= num ^ i
            print(format(mask, '08b'))

        return mask

        # O(nlogn + n)
        # n = len(nums)
        # nums = sorted(nums)

        # for i, num in enumerate(nums):
        #     if num != i:
        #         return i

        # return -1


if __name__ == '__main__':
    input = [9,6,4,2,3,5,7,0,1]
    # input = [3,0,1]
    obj = Solution()
    output = obj.missingNumber(input)
    print('{} - {}'.format(input, output))