"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

From https://leetcode.com/problems/subarray-sum-equals-k/
"""

from collections import defaultdict
from collections import Counter

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # OPTIMIZE
        total = 0
        sum_dict = Counter()
        sum_dict[0] += 1
        cnt = 0

        for i, num in enumerate(nums):
            total += num
            cnt += sum_dict[total - k]
            sum_dict[total] += 1

        return cnt


    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # BRUTE FORCE - O(n**2)

        cnt = 0

        for i in range(len(nums)):
            total = 0

            for num in nums[i:]:
                total += num

                if total == k:
                    cnt += 1

        return cnt


if __name__ == '__main__':
    input = ([1,1,1,5,-3,2,1,3],2)
    # input = ([1],0)
    obj = Solution()
    output = obj.subarraySum(input[0], input[1])
    print('{} - {}'.format(input, output))