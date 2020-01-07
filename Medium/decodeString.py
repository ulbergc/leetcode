"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

from https://leetcode.com/problems/decode-string/
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # getSubString is called once an integer and open bracket have been encountered
        # it ends once a closed bracket is encountered
        # if an integer is encountered first, it recursively calls itself
        def getSubString(i):
            curr = ''
            while i < len(s) and s[i] != ']':
                if s[i].isnumeric():
                    i0 = i
                    # increment i until s[i] is no longer numeric 
                    # - at that point s[i] should equal '['
                    while s[i].isnumeric():
                        i += 1

                    num = s[i0:i]
                    try:
                        num = int(num)
                    except ValueError:
                        print('Oops! {} is not a valid number'.format(num))

                    i, subString = getSubString(i+1)
                    curr += subString * num
                elif s[i].isalpha():
                    curr += s[i]

                i += 1

            return i, curr

        _, newString = getSubString(0)
        return newString


if __name__ == '__main__':
    input = "3[a2[c]]gg"
    # input = "2[abc]3[cd]ef"
    # input = ""
    obj = Solution()
    output = obj.decodeString(input)
    print('{} - {}'.format(input, output))