# T: O(log(n)) if BST is balanced - just like binary search algo. But if not balanced, in worst case: O(n),
# we would essentially have a linked list in this case.
# T: O(h)
# M: O(h)
def search(root, target):
    if not root:
        return False

    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
