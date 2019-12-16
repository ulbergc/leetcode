"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
https://leetcode.com/problems/add-and-search-word-data-structure-design/
"""

from collections import deque

class TrieNode(object):

    def __init__(self, isWord=False):
        self.children = {}
        self.isWord = isWord
            
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        # self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]

        cur.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def _subSearch(node, word):
            if not word:
                return node.isWord

            contains = False
            if word[0] == '.':
                for c in node.children:
                    contains |= _subSearch(node.children[c], word[1:])
                    if contains:
                        return True
            elif word[0] in node.children:
                contains |= _subSearch(node.children[word[0]], word[1:])

            return contains

        return _subSearch(self.root, word)


        # cur = self.root
        # nodes = []
        # nodes.append(cur)

        # for c in word:
        #     # new_nodes = []
        #     # for node in nodes
        #     # if c == '.':
        #     if c not in cur.children:
        #         return False
            
        #     cur = cur.children[c]
        

if __name__ == '__main__':
    input = (1,4)
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    print(obj.search("pad"))
    print(obj.search("bad")) 
    print(obj.search(".ad")) 
    print(obj.search("b.."))
    print(obj.search("b..d"))
    print(obj.search("b."))
    print(obj.search("ba"))
    print(obj.search("..d"))
    print(obj.search("b.d"))
    print(obj.search("..."))
    # print('{} - {}'.format(input, output))