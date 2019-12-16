"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
https://leetcode.com/problems/word-squares/

Build trie out of input words
For each word, test if it is the start of a valid word square
- find words that match its second letter

Recursively:
- Add word to current square
    - Find valid words for the next position
    - add them recursively

"""

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        # build trie out of words
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}

                cur = cur[c]

            cur['end'] = word

        output = []

        def _validPrefixNode(cur):
            new = len(cur)
            pos = 0
            node = trie
            while pos < new:
                if cur[pos][new] in node:
                    node = node[cur[pos][new]]
                    pos += 1
                else:
                    return None

            return node


        def _validWords(node, n, N):
            if n == N and 'end' in node:
                return [node['end']]

            valid = []
            for c in node:
                if c != 'end':
                    valid += _validWords(node[c], n+1, N)

            return valid


        def _addWord(word, cur):
            # any word being input has already been determined to be valid
            # make copy of list
            cur = cur[:]
            cur.append(word)
            if len(cur) == len(word):
                output.append(cur)
                return

            # find the valid prefix at the current position
            node = _validPrefixNode(cur)

            if not node:
                return

            # traverse the rest of the tree to see if any words exist of the correct length, 
            # recursively add them
            valid = _validWords(node, len(cur), len(word))
            for val in valid:
                _addWord(val, cur)


        for word in words:
            _addWord(word, [])

        return output


if __name__ == '__main__':
    # input = ["area","lead","wall","lady","ball"]
    input = ["abat","baba","atan","atal"]
    obj = Solution()
    output = obj.wordSquares(input)
    print('{} - {}'.format(input, output))