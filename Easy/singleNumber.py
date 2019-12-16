"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
https://leetcode.com/problems/single-number/
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # WITH BITS
        cur = 0
        for num in nums:
            cur ^= num
            
        return cur


if __name__ == '__main__':
    input = [4,1,2,1,4]
    obj = Solution()
    output = obj.singleNumber(input)
    print('{} - {}'.format(input, output))