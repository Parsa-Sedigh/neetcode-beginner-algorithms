class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        # left is head
        # right is tail
        self.left = self.right = None

    # O(1)
    def enqueue(self, val):
        newNode = ListNode(val)

        # Queue is non-empty
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = newNode

    # O(1)
    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None

        # Remove left node and return value. Just move the left pointer forward
        val = self.left.val
        self.left = self.left.next

        return val

    def print(self):
        cur = self.left
        while cur:
            print(cur.val, ' -> ', end ="")
            cur = cur.next

        print() # new line