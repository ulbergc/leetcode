"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
https://leetcode.com/problems/trapping-rain-water/submissions/

Use stack
Iterate over each index
- If curr < prev, add prev to stack - add (base, h, ind), formerly (h, index)
- If curr == prev, remove prev from stack (Dont' do!)
- If curr > prev
    - Check stack
    - If prev element higher, fill water to current level

"""
from collections import deque


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = deque()
        water = 0

        for i in range(1,len(height)):
            if height[i] < height[i-1]:
                prev = height[i-1]
                curr = height[i]
                stack.appendleft((height[i], height[i-1], i-1))
                # this code works but takes too long
                # while curr < prev:
                #     stack.appendleft((prev, i-1))
                #     prev -= 1
            elif height[i] > height[i-1]:
                while stack and stack[0][0] < height[i]:
                    prev = stack.popleft()
                    W = (i - prev[2] - 1)
                    if prev[1] <= height[i]:
                        H = prev[1] - prev[0]
                    else:
                        H = (height[i] - prev[0])
                        stack.appendleft((height[i], prev[1], prev[2]))
                    water += W * H
                # this code works but takes too long
                # while stack and stack[0][0] <= height[i]:
                #     prev = stack.popleft()
                #     water += i - prev[1] - 1

        return water

if __name__ == '__main__':
    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    # input = [0,1,0,2,1,0,1,3,2,1,2,2,1,3]
    # input = [5,0,2,0,1,3,5]
    # input = [1,2]
    obj = Solution()
    output = obj.trap(input)
    print('Water = {}'.format(output))