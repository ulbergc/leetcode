"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.
https://leetcode.com/problems/text-justification/

Solution:
do this recursively
- build one line, recursively call on the remaining words, add current line to the result
- break case is if it is the final line
    - in this case, don't right justify

To build a line:
increment thru words, add len(word) + 1 (for space)
- spacesToFill <- keep track of number of spaces (numWords - 1)
- numSpaces = maxWidth - numCharactersInWords (>= numWords - 1)
- numBlanksPerSpace = numSpaces // spacesToFill
- Extra spaces before the line is completed = numSpaces % spacesToFill

"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        def _subJustify(startIndex):
            curLength = 0
            curIndex = startIndex
            while curLength <= maxWidth + 1 and curIndex < len(words):
                curLength += len(words[curIndex]) + 1
                curIndex += 1

            if curLength <= maxWidth + 1:
                # if last line, return
                return [' '.join(words[startIndex:]) + ' ' * (maxWidth - curLength + 1)]
            else:
                # build line and call on the remaining words
                curIndex -= 1
                curLength -= len(words[curIndex]) + 1
                numWords = curIndex - startIndex
                numSpaces = maxWidth - (curLength - numWords)
                if numWords > 1:
                    numBlanksPerSpace = numSpaces // (numWords - 1)
                    extraBlanks = numSpaces % (numWords - 1)
                else:
                    return [words[startIndex] + ' ' * numSpaces] + _subJustify(curIndex)

                line = ''
                for i in range(startIndex, curIndex - 1):
                    line += words[i] + (' ' * numBlanksPerSpace)
                    if extraBlanks:
                        line += ' '
                        extraBlanks -= 1

                line += words[curIndex - 1]

                return [line] + _subJustify(curIndex)

        return _subJustify(0)
        

if __name__ == '__main__':
    # input = (["What","must","be","acknowledgment","shall","be"], 16)
    input = (["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20)
    obj = Solution()
    output = obj.fullJustify(input[0], input[1])
    print('{} - {}'.format(input, output))
    topLine = ''
    for i in range(input[1]):
        topLine += str(i % 10)
    print(topLine)
    for line in output:
        print('{}.'.format(line))