"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

*** APPROACH ***
backtracking (recursive)
- go until you find a word (keep track of start and end index)
- if you find one, call again at the new position
- if you fail, backtrack to the previous position
    - try to extend the word

From https://leetcode.com/problems/word-break/
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        visited = set()
        n = len(s)

        def backtrack(head, tail):
            pos = (head, tail)
            if pos in visited:
                return False

            visited.add(pos)

            while tail < n:
                if s[head:tail] in wordSet:
                    break
                tail += 1

            if tail == n:
                result = s[head:tail] in wordSet
            elif not backtrack(tail, tail + 1):
                # try increasing tail again
                result = backtrack(head, tail + 1)
            else:
                result = True

            return result

        return backtrack(0, 1)


if __name__ == '__main__':
    # input = ("catsandog",["cats", "dog", "sand", "and", "cat"])
    input = ("aaaaaaaaaaab",["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"])
    # input = ("applepenapple",["apple", "pen"])
    obj = Solution()
    output = obj.wordBreak(input[0], input[1])
    print('{} - {}'.format(input, output))