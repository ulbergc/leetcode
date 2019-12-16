"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

In deserialize:
- create list of vals (1-indexed for easy manipulation)
- then call _addNode(cur=0), which will:
    - Create a new node, with the value at vals[cur]
    - assign left and right nodes to be new nodes
        - new nodes created with _addNode(left(cur), right(cur))
        - left(cur) = cur * 2 ; right(cur) = cur * 2 + 1
    - if cur is greater than length of array, end
    - if vals[cur-1] is None, end (doesn't allow for nodes with node.val = None)

*** Modification to _addNode() to prevent excessive storage:
keep track of index adjustment for vals array
*** instead of recursive deserialization, do breadth-first, like in serialization
for each level:
- keep track of number of valid nodes (not None) - current node is indValid (0-indexed)
- there will be numValid * 2 in the next level
  for a given node:
  - its children will be (index at end of prev level + 1) + [indValid*2, indValid*2+1]

*** do a first pass through array, recording:
- level #
- number of valid nodes per level
- index of start of level

Create another array containing the location of the children for a given node

"""
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CodecLarge:
    """This version is inefficient.
    In the worst case scenario, a completely unbalanced, linear tree,
    storage will be 2^n - 1 instead of n (2*n)
    In the best case, storage will be best case (n = 2^maxLevel - 1)
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res = []
        queue = collections.deque()
        queue.append((root, 1))
        curLevel = 0
        levelHasNode = True

        while queue:
            node, level = queue.popleft()
            if level > curLevel:
                if not levelHasNode:
                    break
                levelHasNode = False
                curLevel = level

            if node:
                val, left, right = node.val, node.left, node.right
                if left or right:
                    levelHasNode = True
            else:
                val, left, right = None, None, None
            
            res.append(val)
            queue.append((left, level + 1))
            queue.append((right, level + 1))

        return str(res).replace(' ', '')


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 3:
            return None
        
        vals = data[1:-1].split(',')
        n = len(vals)

        def _addNode(cur):
            if cur > n:
                return None

            val = vals[cur - 1]
            if val == 'None':
                return None
            else:
                val = int(val)

            node = TreeNode(val)
            node.left = _addNode(cur * 2)
            node.right = _addNode(cur * 2 + 1)
            return node

        return _addNode(1)

        
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return '[]'

        res = []
        queue = collections.deque()
        queue.append((root, 1))
        curLevel = 0
        levelHasNode = True

        while queue:
            node, level = queue.popleft()
            if level > curLevel:
                if not levelHasNode:
                    break
                levelHasNode = False
                curLevel = level

            if node:
                val = node.val
                if node.left or node.right:
                    levelHasNode = True
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
            else:
                val = None

            res.append(val)

        return str(res).replace(' ', '')


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 3:
            return None
        
        vals = data[1:-1].split(',')
        n = len(vals)
        
        # first pass to get information about each level
        startInd = 1
        curLevel = 1
        numValid = 1
        # children = [None] * n
        children = [-1] * n
        while startInd - 1 + numValid <= n:
            numNone = 0
            for i in range(numValid):
                if vals[startInd + i - 1] == 'None':
                    numNone += 1
                    # children[startInd + i - 1] = -1
                # else:
                children[startInd + i - 1] = startInd + numValid + (i - numNone) * 2

            curLevel += 1
            startInd += numValid
            numValid = (numValid - numNone) * 2

        def _addNode(cur):
            if cur > n or cur < 0:
                return None

            val = vals[cur - 1]
            if val == 'None':
                return None
            
            val = int(val)
            node = TreeNode(val)
            node.left = _addNode(children[cur - 1])
            node.right = _addNode(children[cur- 1] + 1)
            return node

        return _addNode(1)


if __name__ == '__main__':
    codec = Codec()
    codec2 = CodecLarge()
    # input = ""
    # input = "[1,None,3,None,None,4,5]"
    # input = "[1,None,3,None,None,4,5,None,None,None,None,None,None,None,6]"
    # input = "[1,None,2,None,None,6,3,None,None,None,None,None,None,None,4]"
    # input = "[1,2,3,None,4,5,6,None,None,7,None,None,8,None,9,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,10]"
    input = "[]"
    # root = codec2.deserialize(input)
    # output = codec.serialize(root)
    # root2 = codec.deserialize(output)
    root2 = codec.deserialize(input)
    output2 = codec.serialize(root2)
    # output = codec.deserialize(codec.serialize(root))
    # print('{} - {} - {}'.format(input, output, output2))
    print('{} - {}'.format(input, output2))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))