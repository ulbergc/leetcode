"""
Look in sets of three, keep track of current power (10 ^ [0,3,6,9,12])
Helper function that returns the set of three answer
Dictionary mapping digits to words
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        thousands = ['', 'Thousand', 'Million', 'Billion']
        ans = ''
        count = 0
        while num > 0 and count < 4:
            tmp = num % 1000
            if tmp > 0:
                ans = ' '.join([self.threeDigitToWords(tmp), thousands[count], ans])
                ans = ans.strip()

            count += 1
            num = num // 1000

        return ans


    def threeDigitToWords(self, num):
        num_dict = {0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', 
                    5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 
                    10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen',
                    15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen',
                    20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty',
                    60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
        below100 = num % 100
        ans = ''
        if below100 < 20:
            ans = num_dict[below100]
        else:
            ans = ' '.join([num_dict[int(10 * (below100 // 10))], num_dict[below100 % 10]])
        
        if num >= 100:
            ans = ' '.join([num_dict[int(num // 100)], 'Hundred', ans])

        ans = ans.strip()
        return ans


if __name__ == '__main__':
    input = 50868
    obj = Solution()
    output = obj.numberToWords(input)
    print(output)