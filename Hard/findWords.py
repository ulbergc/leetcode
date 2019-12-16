"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
https://leetcode.com/problems/word-search-ii/

Solution:
Brute force
- for each word, search the whole board for the starting letter
    - then each adjacent node for the subsequent one, and so on...
    - need to keep track of previously visited nodes in this case so that they aren't revisited

Trie
- build trie out of dictionary
- traverse grid one-by-one. If letter is in trie, begin search

"""
class Trie(object):

    def __init__(self):
        self.root = {}

    
    def getRoot(self):
        return self.root


    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}

            cur = cur[c]

        cur['end'] = True


    def search(self, word, cur):
        for c in word:
            if c not in cur:
                return None
            
            cur = cur[c]

        return cur


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        wordSet = set(words)
        for word in words:
            trie.insert(word)

        R = len(board)
        C = len(board[0])

        res = set()
        def _search(S, cur, prev, node):
            i, j = cur
            new_node = trie.search(board[i][j], cur=node)
            if new_node:
                S += board[i][j]
                if S in wordSet:
                    res.add(S)

                new_prev = prev.copy()
                new_prev.add(cur)
                # search each direction (not trying prev)
                # up
                if i > 0 and (i-1, j) not in prev:
                    _search(S, (i-1, j), new_prev, new_node)
                # right
                if j < C-1 and (i, j+1) not in prev:
                    _search(S, (i, j+1), new_prev, new_node)
                # down
                if i < R-1 and (i+1, j) not in prev:
                    _search(S, (i+1, j), new_prev, new_node)
                # left
                if j > 0 and (i, j-1) not in prev:
                    _search(S, (i, j-1), new_prev, new_node)

        for i in range(R):
            for j in range(C):
                _search('', (i, j), set(), trie.getRoot())

        return list(res)
        

if __name__ == '__main__':
    # input = ([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ["oat","oath","pea","eat","rain"])
    input = ([["a","a"]], ["aaa"])
    obj = Solution()
    output = obj.findWords(input[0], input[1])
    print('{} - {}'.format(input, output))