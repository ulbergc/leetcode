"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
https://leetcode.com/problems/jump-game/
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        lastGood = n - 1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= lastGood:
                lastGood = i

        return lastGood == 0



    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        memo = {n-1:True}

        def _helper(ind):
            if ind in memo:
                return memo[ind]

            if nums[ind] == 0:
                memo[ind] = False
                return memo[ind]

            res = False
            cur = min(nums[ind], n - 1 - ind)
            while cur > 0:
                res = _helper(ind + cur)
                cur -= 1
                if res:
                    memo[ind] = True
                    return memo[ind]

            memo[ind] = False
            return memo[ind]
        
        ans = _helper(0)
        return ans
        

if __name__ == '__main__':
    input = [2,3,1,1,4]
    # input = [3,2,1,0,4]
    obj = Solution()
    output = obj.canJump(input)
    print('{}: {}'.format(input, output))