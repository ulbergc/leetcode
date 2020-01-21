"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.

From https://leetcode.com/problems/minimum-time-difference/
"""

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints = sorted(timePoints)
        n = len(timePoints)

        def getHrMn(t):
            return int(t[0:2]), int(t[3:])


        def timeDiff(t1, t2):
            if t2 < t1:
                t1, t2 = t2, t1
            hr1, mn1 = getHrMn(t1)
            hr2, mn2 = getHrMn(t2)

            time_diff = (hr2 - hr1) * 60 + (mn2 - mn1)

            if time_diff > 12 * 60:
                time_diff = (hr1 + 24 - hr2) * 60 + (mn1 - mn2)

            return time_diff


        min_time = 12*60
        for i in range(n):
            min_time = min(timeDiff(timePoints[i], timePoints[(i+1) % n]), min_time)

        return min_time


if __name__ == '__main__':
    # input = ["23:59","00:00"]
    input = ["23:59","00:00","13:45","01:12"]
    obj = Solution()
    output = obj.findMinDifference(input)
    print('{} - {}'.format(input, output))