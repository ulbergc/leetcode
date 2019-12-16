"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
https://leetcode.com/problems/bitwise-and-of-numbers-range/

This will usually be 0, unless the most significant bit is the same for m and n
In that case, the answer is the most significant bit
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1

        return n << i

        # A LITTLE BETTER
        # def _getBits(num):
        #     bits = []
        #     pos = 0
        #     while num > 0:
        #         if num & 1:
        #             bits.append(pos)

        #         num >>= 1
        #         pos += 1

        #     return bits

        # m_bits = _getBits(m)
        # n_bits = _getBits(n)

        # i = len(m_bits) - 1
        # j = len(n_bits) - 1

        # ans = 0
        # while i >= 0 and j >= 0:
        #     if m_bits[i] == n_bits[j]:
        #         ans += 1 << m_bits[i]
        #         i -= 1
        #         j -= 1
        #     else:
        #         break

        # return ans


        # INEFFICIENT
        # def _getMSB(num):
        #     msb = 1
        #     while num > 0:
        #         num >>= 1
        #         msb <<= 1
        #     return msb >> 1

        # ans = 0
        # mx = _getMSB(m) 
        # nx = _getMSB(n) 
        # while mx > 0 and nx > 0:
        #     mx = _getMSB(m) 
        #     nx = _getMSB(n)
        #     if mx == nx:
        #         ans += mx
        #         m -= mx
        #         n -= nx
        #     else:
        #         break

        # return ans
        

if __name__ == '__main__':
    input = [13,15]
    obj = Solution()
    output = obj.rangeBitwiseAnd(input[0], input[1])
    print('{} - {}'.format(input, output))