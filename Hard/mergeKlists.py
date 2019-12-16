"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def _printList(node):
            vals = []
            while node:
                vals.append(node.val)
                node = node.next

            return vals

        
        def _merge2Lists(a, b):
            # make sure a.val is <= b.val
            if b.val < a.val:
                b, a = a, b
                
            head = a
            tail = a
            a = a.next
            
            while a and b:
                if a.val < b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next
                tail = tail.next

            if a:
                tail.next = a
            else:
                tail.next = b

            return head
    
        while len(lists) > 1:
            new_lists = []
            for i in range(0,len(lists)-1,2):
                new_lists.append(_merge2Lists(lists[i], lists[i+1]))
                
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])
                
            lists = new_lists
            
        return lists[0]


    def merge2Lists(self, a, b):
        # make sure a.val is <= b.val
        if b.val < a.val:
            b, a = a, b
            
        head = a
        tail = a
        a = a.next
        
        while a and b:
            print(head.val, tail.val)
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        if a:
            tail.next = a
        else:
            tail.next = b

        return head


    def makeList(self, vals):
        # vals = [1,4,5]
        cur = 0
        head = ListNode(0)
        tail = head
        while cur < len(vals):
            node = ListNode(vals[cur])
            tail.next = node
            tail = node
            cur += 1

        return head.next


if __name__ == '__main__':
    input = [1,2,3,4]
    obj = Solution()
    lists = []
    lists.append(obj.makeList([1,4,5]))
    lists.append(obj.makeList([2,3,4]))
    lists.append(obj.makeList([2,6]))

    # A = obj.merge2Lists(lists[0], lists[1])
    B = obj.mergeKLists(lists)
    B

    # output = obj.productExceptSelf(input)
    # print('{} - {}'.format(input, output))