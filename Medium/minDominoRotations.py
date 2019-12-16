"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

breadth-first search, with a queue
    - This builds up a 'path' that is taken to the answer
    - store visited states
        - set of tuples with indices of flipped dominoes
Rule: don't reflip the same domino
    - keep track of previous moves on a given path

Simpler: 
- 1. find the number that will be the same
- 1a. if it doesn't exist, return -1
- 2. Count times that number is in A and B, take the max (x = max(count A, count B))
- answer = min(N-x, x)

- combine 1 and 2 into the same loop
"""
import collections

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        count_dict = {}
        
        if A[0] == B[0]:
            count_dict[A[0]] = collections.Counter({'A':1, 'B':1})
        else:
            count_dict[A[0]] = collections.Counter({'A':1, 'B':0})
            count_dict[B[0]] = collections.Counter({'A':0, 'B':1})

        for i in range(1,len(A)):
            rm_val = []
            for val in count_dict:
                # verify number is on all of the dominos
                if val != A[i] and val != B[i]:
                    rm_val.append(val)
                # Increment count
                if A[i] == val:
                    count_dict[val]['A'] += 1
                if B[i] == val:
                    count_dict[val]['B'] += 1

            for val in rm_val:
                del count_dict[val]

            if not count_dict:
                return -1
        
        val, counter = count_dict.popitem()
        max_num = max(counter.values())
        return min(len(A) - max_num, max_num)

if __name__ == '__main__':
    # input = ([2,1,2,4,2,2], [5,2,6,2,3,2])
    # input = ([3,5,1,2,3], [3,6,3,3,4])
    input = ([3,5,6], [5,3,3])
    obj = Solution()
    output = obj.minDominoRotations(input[0], input[1])
    print('{} - {}'.format(input, output))