"""
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
https://leetcode.com/problems/integer-to-roman/
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        roman = {1:'I', 4:'IV', 5:'V', 9: 'IX', 10:'X', 40:'XL', 50:'L', 
                90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        

        def _findLargestRoman(n):
            # roman_nums = [1000, 500, 100, 50, 10, 5, 1]
            roman_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            i = 0
            while roman_nums[i] > n:
                i += 1
                
            return roman_nums[i]
            

        ans = ''
        
        while num > 0:
            cur = _findLargestRoman(num)
            ans += roman[cur]
            num -= cur

        return ans


if __name__ == '__main__':
    input = 499
    obj = Solution()
    output = obj.intToRoman(input)
    print('{}: {}'.format(input, output))