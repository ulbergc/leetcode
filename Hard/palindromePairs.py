"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]

From https://leetcode.com/problems/palindrome-pairs/

*** APPROACH ***
Brute force method - check every pair - is it a palindrome?
Trie method
- build two tries: forward and backward
- check each forward word
    - continue as long as you can also go backwards
    - two success conditions:
        - if you reach the end of both directions and they are still valid (same length)
        - if you reach the end of one direction first
            - subcheck to see that the remainder of the other word is a palindrome
Trie updated
- only need one trie going backwards?
    - two cases if words are different lengths
        - [CASE 1] backward is shorter - check remainder of word
        - [CASE 2] forward is shorter - check remainder of trie
"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ans = []

        def addToTrie(trie, word, index):
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {'#':[]}

                curr['#'].append(index)
                curr = curr[c]

            curr['#'].append(index)
            curr['END'] = index


        def checkIsPalindrome(word):
            head, tail = 0, len(word) - 1
            while head < tail:
                if word[head] != word[tail]:
                    return False
                
                head += 1
                tail -= 1

            return True


        # build backwards trie
        backward = {'#':[]}
        for i, word in enumerate(words):
            addToTrie(backward, word[::-1], i)

        # now check each word
        for i, word in enumerate(words):
            curr = backward
            legit, pos = True, -1
            for pos, c in enumerate(word):
                if 'END' in curr:
                    # CASE 1
                    # check remainder of word
                    # if checkTailPalindrome(word, pos):
                    if curr['END'] != i and checkIsPalindrome(word[pos:]):
                        ans.append([i, curr['END']])

                if c not in curr:
                    legit = False
                    break
                else:
                    curr = curr[c]

            # CASE 2
            # check remainder of trie branch (beginning of words[j])
            if legit:
                for j in curr['#']:
                    if i != j and checkIsPalindrome(words[j][:len(words[j]) - pos - 1]):
                        ans.append([i, j])

        return ans

            

if __name__ == '__main__':
    input = ["abcd","dcba","lls","s","sssll","abc","abcde"]
    # input = ["abcd","dcba","lls","s","sssll"]
    input = ["a","abc","aba",""]
    obj = Solution()
    output = obj.palindromePairs(input)
    print('{} - {}'.format(input, output))