"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

*** APPROACH ***
Do postorder traversal (left, right, root)
For a given node, calculate its max as left + right + root
    - only include left and right if they are > 0
When returning max path to parent, only include one-sided path
    - This mean calculate the max at a given node with potentially both l and r
    - But return only one side (the largest)
Keep a global maxValue variable that is updated if the current val is greater
    - maxValue = max(maxValue, currVal)

From https://leetcode.com/problems/binary-tree-maximum-path-sum/
Difficulty Hard
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def findMax(node):
            # initialize in case children are None
            leftMax, rightMax = node.val, node.val
            leftVal, rightVal = 0, 0

            if node.left:
                leftMax, leftVal = findMax(node.left)

            if node.right:
                rightMax, rightVal = findMax(node.right)

            oneSide = node.val + max(leftVal, rightVal, 0)
            twoSide = node.val + max(leftVal, 0) + max(rightVal, 0)
            return max(twoSide, leftMax, rightMax), oneSide

                
        maxValue, _ = findMax(root)
        return maxValue
        

    def makeTree(self, vals):
        nodes = [None] * len(vals)

        for i in range(len(vals)-1, -1, -1):
            if vals[i]:
                nodes[i] = TreeNode(vals[i])
                l = i * 2 + 1
                r = i * 2 + 2
                if r < len(vals):
                    nodes[i].left = nodes[l]
                    nodes[i].right = nodes[r]

        return nodes[0]


if __name__ == '__main__':
    # input = [-10,9,20,None,None,15,7]
    # input = [-10,9,-8,None,None,15,7]
    # input = [1,2,3]
    input = [5,4,8,11,None,13,4,7,2,None,None,None,None,None,1]

    obj = Solution()
    root = obj.makeTree(input)
    output = obj.maxPathSum(root)
    print('{} - {}'.format(input, output))