"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
https://leetcode.com/problems/minimum-window-substring/

Keep pointers to head and tail of current substring
Keep set of current letters that are required to complete a valid substring
    - At beginning, this will be all of the letters from string T
    - Later, you remove the first letter, and search for its next occurence
Two cases where you increment pointers: head and tail
    Increment tail:
        - do this when you are searching for letters to complete a valid substring
            - remove letter from search_set when found. 
                - once search_set is empty, you have a valid substring
            - If you find a letter that you've already found in char_dict:
                - update the index of that letter in char_dict
                    - you will always have the most recent occurrence (furthest right)
                - If that letter is the current head of your substring, increment head
    Increment head:
        - Two cases: 
            - finding a new substring
            - encounter the current head when incrementing tail
        - In both cases, the process is the same - find the next valid start point
            - This can be done by incrementing head until you find a letter at the correct position in char_dict
            - Or possible use a queue and just jump straight to the next valid location?
                - This would be complicated when you update a letter's position
        
"""

class Solution(object):
    # BEST
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        
    # BETTER
    def minWindow1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # initialize values
        char_dict = {}
        search_dict = {}
        target_dict = {}
        for c in t:
            if c not in char_dict:
                char_dict[c] = [-1]
            if c not in search_dict:
                search_dict[c] = 0
                target_dict[c] = 0
            search_dict[c] += 1
            target_dict[c] += 1

        cur_shortest = (0, len(s)+1)

        # find first valid letter
        head = 0
        while head < len(s) and s[head] not in char_dict:
            head += 1

        if head == len(s):
            return ''
        else:
            char_dict[s[head]] = [head]
        
        def _incrementHead(cur):
            # This assumes there is a valid target
            while cur < len(s):
                if s[cur] in char_dict and char_dict[s[cur]][0] == cur:
                    break
                cur += 1
            
            return cur

        tail = head
        while tail < len(s):
            if s[tail] in search_dict:
                if search_dict[s[tail]] == 1:
                    del search_dict[s[tail]]
                else:
                    search_dict[s[tail]] -= 1
            
            if s[tail] in char_dict:
                prev_ind = char_dict[s[tail]][0]
                if prev_ind == -1:
                    char_dict[s[tail]] = [tail]
                else:
                    char_dict[s[tail]].append(tail)
                if len(char_dict[s[tail]]) > target_dict[s[tail]]:
                    char_dict[s[tail]].pop(0)
                if prev_ind == head:
                    head = _incrementHead(head)

            # If search_dict is empty, check cur_shortest, update head
            if not search_dict:
                # update cur_shortest if necessary
                cur_length = tail - head + 1
                if cur_length < cur_shortest[1]:
                    cur_shortest = (head, cur_length)

                if cur_length == len(t):
                    break

                # add s[head] to search_dict, then remove and increment head
                search_dict[s[head]] = 1

                if target_dict[s[head]] == 1:
                    char_dict[s[head]] = [-1]
                else:
                    char_dict[s[head]].pop(0)
                head = _incrementHead(head)

            tail += 1

        if cur_shortest[1] > len(s):
            return ''
        else:
            return s[cur_shortest[0]:(cur_shortest[0] + cur_shortest[1])]


    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # initialize values
        char_dict = {x:-1 for x in t}
        search_set = set(char_dict.keys())
        cur_shortest = (0, len(s)+1)

        # find first valid letter
        head = 0
        while head < len(s) and s[head] not in char_dict:
            head += 1

        if head == len(s):
            return ''
        else:
            char_dict[s[head]] = head
        
        def _incrementHead(cur):
            # This assumes there is a valid target
            while cur < len(s):
                if s[cur] in char_dict and char_dict[s[cur]] == cur:
                    break
                cur += 1
            
            return cur

        tail = head
        while tail < len(s):
            if s[tail] in search_set:
                search_set.remove(s[tail])
            
            if s[tail] in char_dict:
                prev_ind = char_dict[s[tail]]
                char_dict[s[tail]] = tail
                if prev_ind == head:
                    head = _incrementHead(head)

            # If search_set is empty, check cur_shortest, update head
            if not search_set:
                # update cur_shortest if necessary
                cur_length = tail - head + 1
                if cur_length < cur_shortest[1]:
                    cur_shortest = (head, cur_length)

                if cur_length == len(t):
                    break

                # add s[head] to search_set, increment head
                search_set.add(s[head])
                char_dict[s[head]] = -1
                head = _incrementHead(head)

            tail += 1

        if cur_shortest[1] > len(s):
            return ''
        else:
            return s[cur_shortest[0]:(cur_shortest[0] + cur_shortest[1])]


if __name__ == '__main__':
    # input = ("ADOBECODEBANC", "ABC")
    # input = ("ADOBECODEBANCAABEFBABACEBA", "ABC")
    input = ("ADOBECODEBANCAABEFBABACEBA", "AAB")
    obj = Solution()
    output = obj.minWindow(input[0], input[1])
    print('{} - {}'.format(input, output))