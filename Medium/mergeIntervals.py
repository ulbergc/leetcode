"""
Given a collection of intervals, merge all overlapping intervals.
https://leetcode.com/problems/merge-intervals/
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals
        
        # first sort
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        result = []

        cur = 0
        while cur < len(intervals):
            # merge all intervals that overlap with intervals[cur]
            point = cur + 1
            while point < len(intervals) and intervals[cur][1] >= intervals[point][0]:
                intervals[cur][1] = max(intervals[cur][1], intervals[point][1])
                point += 1
            
            result.append([intervals[cur][0], intervals[cur][1]])
            cur = point

        return result


if __name__ == '__main__':
    # input = [[1,3],[2,6],[8,10],[15,18],[2,14]]
    input = []
    obj = Solution()
    output = obj.merge(input)
    print('{} - {}'.format(input, output))