class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# T: O(n)
# Since the algorithm traverses each node exactly once and performs constant-time operations, its time complexity
# is O(n), where n is the number of nodes in the tree.

# M: O(n)
def canReachLeaf(root):
    # base case
    # Note: Null node(out of bounds) is not a leaf node. The case: `If not root` could happen if we went
    # out of bounds from a node that has one child. The node is not considered a leaf node because it has a child.
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:
        return True

    if canReachLeaf(root.left):
        return True

    if canReachLeaf(root.right):
        return True

    return False

# T: O(n)
# M: O(n)
def leafPath(root, path):
    if not root or root.val == 0:
        return False

    path.append(root.val)

    if not root.left and not root.right:
        return True

    # we're not creating a new copy of path variable, we're passing the reference to it to this func call.
    # It works the same in most langs.
    if leafPath(root.left, path):
        return True

    if leafPath(root.right, path):
        return True

    # we have to backtrack
    path.pop()

    return False