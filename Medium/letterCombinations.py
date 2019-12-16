"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

- loop through each digit (forward/backward?)
- for each corresponding character, append/prepend to current
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
            
        num_pad = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        combos = ['']
        for digit in digits:
            new_combos = []
            for char in num_pad[digit]:
                for combo in combos:
                    new_combos.append(combo + char)

            combos = new_combos

        return combos


if __name__ == '__main__':
    input = "236"
    obj = Solution()
    output = obj.letterCombinations(input)
    print('{} - {}'.format(input, output))