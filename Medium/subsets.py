"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
https://leetcode.com/problems/subsets/
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        for i in range(1 << len(nums)):
            sub = []
            bit = i
            pos = 0
            while bit > 0:
                if bit & 1:
                    sub.append(nums[pos])
                pos += 1
                bit >>= 1
            ans.append(sub)

        return ans


if __name__ == '__main__':
    input = [3,33,14]
    obj = Solution()
    output = obj.subsets(input)
    print('{} - {}'.format(input, output))