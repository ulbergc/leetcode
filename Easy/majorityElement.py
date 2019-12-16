"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
https://leetcode.com/problems/majority-element/
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 0
            num_dict[num] += 1

            if num_dict[num] > n//2:
                return num
        
        return -1
        

if __name__ == '__main__':
    # input = [2,2,1,1,1,2,2,3,2]
    input = [3,2,3]
    obj = Solution()
    output = obj.majorityElement(input)
    print('{} - {}'.format(input, output))