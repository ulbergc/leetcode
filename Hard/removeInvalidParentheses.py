"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).
https://leetcode.com/problems/remove-invalid-parentheses/
"""

import collections

class Solution(object):
    def removeInvalidParentheses0(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def _hasValidParentheses(check):
            stack = 0

            for c in check:
                if c == '(':
                    stack += 1
                if c == ')':
                    if stack == 0:
                        return False
                    stack -= 1
                    
            return stack == 0

        if _hasValidParentheses(s):
            return [s]

        queue = collections.deque()
        queue.append((0, s))
        cur_level = 0

        result = set()
        while queue:
            level, cur = queue.popleft()

            if level > cur_level:
                cur_level += 1
                if result:
                    return list(result)

            if _hasValidParentheses(cur):
                result.add(cur)

            for i in range(len(cur)):
                if cur[i] in '()':
                    queue.append((level + 1, cur[:i] + cur[i+1:]))

        # return all the characters except '()'
        return [cur]

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def _hasValidParentheses(check):
            stack = 0

            for c in check:
                if c == '(':
                    stack += 1
                if c == ')':
                    if stack == 0:
                        return False
                    stack -= 1
                    
            return stack == 0

        if _hasValidParentheses(s):
            return [s]

        queue = collections.deque()
        queue.append((0, s))
        cur_level = 0

        result = set()
        visited = set()
        while queue:
            level, cur = queue.popleft()

            if level > cur_level:
                cur_level += 1
                if result:
                    return list(result)

            if _hasValidParentheses(cur):
                result.add(cur)

            for i in range(len(cur)):
                if cur[i] in '()':
                    new = cur[:i] + cur[i+1:]
                    if new not in visited:
                        queue.append((level + 1, new))
                        visited.add(new)

        # return all the characters except '()'
        return [cur]
        

if __name__ == '__main__':
    input = "(a)())()"
    input = "()(((((((()"
    obj = Solution()
    output = obj.removeInvalidParentheses(input)
    print('{} - {}'.format(input, output))