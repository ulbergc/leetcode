"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
https://leetcode.com/problems/find-the-celebrity/
"""


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):
    def __init__(self):
        self.graph = [
                [1,1,0,1],
                [0,1,1,1],
                [1,1,1,1],
                [0,0,0,1]
                ]

    def knows(self, a, b):
        if self.graph[a][b] == 1:
            return True
        else:
            return False


    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1

        def _isCelebrity(i):
            for j in range(n):
                if j == i:
                    continue
                # does everybody know them?
                if not self.knows(j, i):
                    return -1 
                # do they know anybody?
                if self.knows(i, j):
                    return -1

            return i

        possible = set(range(n))

        while len(possible) > 1:
            person1 = possible.pop()
            possible_new = set()
            num_known = 0
            for person2 in possible:
                if self.knows(person1, person2):
                    num_known += 1
                    possible_new.add(person2)

            if num_known == 0:
                possible_new.add(person1)

            possible = possible_new

        # now do a full check on this person
        person = possible.pop()
        return _isCelebrity(person)

        # BRUTE FORCE
        # for i in range(n):
        #     num_known = 0
        #     for j in range(n):
        #         num_known += self.knows(i,j)
        #         if num_known > 1:
        #             break
                
        #     if num_known == 1:
        #         return 1
        
        # return -1


if __name__ == '__main__':
    input = 3
    obj = Solution()
    output = obj.findCelebrity(input)
    print('{} - {}'.format(input, output))