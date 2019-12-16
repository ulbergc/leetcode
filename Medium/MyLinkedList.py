"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
https://leetcode.com/problems/design-linked-list/
"""

class MyNode(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None
        

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = MyNode('H')
        self.size = 0

    
    def fetchNode(self, index):
        if index > self.size - 1:
            return None

        curr = self.head
        pos = -1
        while pos < index:
            curr = curr.next
            pos += 1

        return curr
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node = self.fetchNode(index)
        if not node:
            ans = -1
        else:
            ans = node.val
        return ans
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        curr = self.fetchNode(index - 1)
        if curr:
            newNode = MyNode(val)
            newNode.next = curr.next
            curr.next = newNode
            self.size += 1


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        curr = self.fetchNode(index - 1)

        if curr and curr.next:
            curr.next = curr.next.next
            self.size -= 1
        

    def printLinkedList(self):
        curr = self.head

        output = ''
        while curr:
            output += '({})-'.format(curr.val)
            curr = curr.next

        output += '(X)'
        print(output)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

def main():
    obj = MyLinkedList()
    obj.printLinkedList()
    obj.addAtHead(1)
    obj.printLinkedList()
    obj.addAtTail(3)
    obj.printLinkedList()
    obj.addAtIndex(1,2)
    obj.printLinkedList()
    obj.get(1)
    obj.printLinkedList()
    obj.deleteAtIndex(1)
    obj.printLinkedList()
    obj.get(1)
    obj.printLinkedList()

if __name__ == '__main__':
    main()
    
    