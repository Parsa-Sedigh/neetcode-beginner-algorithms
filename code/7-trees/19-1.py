class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# T: O(h) - usually h is log(n), So O(log(n)) if we have a balanced tree.

# As we traverse the tree, we're either gonna go left or right, we're not gonna go both ways. So
# in worst case, we're gonna visit one node for every level of the tree.

# M: O(h)- usually h is log(n), so O(log(n)).

# This is because the algorithm uses recursion, and the space required for the recursion stack is proportional to
# the height of the tree.

# Insert a new node and return the root of the BST
def insert(root, val):
    if not root:
        # Create the new node and return it to the caller
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)

    return root

# Return the minimum value node of the BST.
def minValueNode(root):
    # We don't have to create a new var. We can use the func param itself.
    curr = root

    # We don't want to go out of bounds. We want to finish at the last node. So we check for both `curr and curr.left` .
    # If we wanted to go out of bounds, we would only check for `curr`.
    # As we go in one direction, we're essentially traversing a linked list.
    while curr and curr.left:
        curr = curr.left

    return curr

# Remove a node and return the root of the BST.
# T: O(log(n))
def remove(root, val):
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val

            # Currently, we have two copies of whatever node the minValueNode() returned, so we have to remove it. So
            # call remove() again on the right subtree. The good thing here is: Since we found the minimum val from
            # the right subtree, we know that node has at most one child, but it won't have two children(since we get
            # the minimum value and we know BST doesn't have duplicates). So the second time we call remove() which
            # is what we're gonna do in the next line, it's gonna be the simple case(0 or 1 child case) and in this
            # case, it's gonna have at most 1 RIGHT child(since we grabbed the minimum val which would be in the left).
            # Since it would be the simple case of remove(), we won't have anymore recursive calls in the next remove().
            root.right = remove(root.right, minNode.val)

    return root