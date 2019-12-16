"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.
https://leetcode.com/problems/replace-words/
"""

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        words = sentence.split()
        trie = self.buildTrie(dict)
        new_sentence = []

        for word in words:
            # if word has prefix in dict, append prefix, else, append word
            new_sentence.append(self.searchTrie(trie, word))

        return ' '.join(new_sentence)


    def buildTrie(self, dict):
        head = {}
        for prefix in dict:
            self.insertNode(head, prefix)
        
        return head


    def insertNode(self, head, prefix):
        cur = head
        for c in prefix:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]

        cur['full'] = prefix


    def searchTrie(self, trie, word):
        cur = trie

        for c in word:
            if c not in cur:
                return word

            cur = cur[c]
            if 'full' in cur:
                return cur['full']

        return word


if __name__ == '__main__':
    input = (["cat", "bat", "rat"], "the cattle was rattled by the battery")
    obj = Solution()
    output = obj.replaceWords(input[0], input[1])
    print('{} - {}'.format(input, output))