class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


# Implementation for Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        # the next node after head, should point to the newNode
        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = ListNode(val)

        # self.tail is a dummy node and should always remain the last node in the linked list. Therefore, we should point the
        # `next` field of newNode to self.tail .
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        # this line sets the next field of the previous node of newNode.
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

        # approach 2
        # node2 = self.tail.prev
        # node2.next = None
        # tail = node2

    def print(self):
        curr = self.head.next

        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next

        print()
