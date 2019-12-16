"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        R = 1
        for i in range(1, n):
            R *= nums[n-i]
            ans[n-i-1] *= R

        return ans


        # EXTRA SPACE
        # n = len(nums)
        # prod_from_right =  [0] * n
        # prod_from_left = [0] * n
        # prod_from_right[n - 1] = 1
        # prod_from_left[0] = 1
        
        # for i in range(1, n):
        #     prod_from_left[i] = prod_from_left[i-1] * nums[i-1]
        #     prod_from_right[n-i-1] = prod_from_right[n-i] * nums[n-i]
            
        # return [prod_from_right[i]*prod_from_left[i] for i in range(n)]


if __name__ == '__main__':
    input = [1,2,3,4]
    obj = Solution()
    output = obj.productExceptSelf(input)
    print('{} - {}'.format(input, output))