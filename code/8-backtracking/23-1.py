class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# T: O(n)
# Since the algorithm traverses each node exactly once and performs constant-time operations, its time complexity
# is O(n), where n is the number of nodes in the tree.
# Note: We don't have a two-way branch recursion here. Yes, we have two ways to go at each node, but we don't have duplicate work
# to do at each node. Meaning we will visit each node only once. So time is O(n) not O(2^h) and M is also O(n).

# M: O(h).
def canReachLeaf(root) -> bool:
    # base case

    # The base case is we reach a null node or we reach a node with the value zero. But we do have another base case which is when
    # we get to a leaf node

    # Note: Null node(out of bounds) is not a leaf node. The case: `If not root` could happen if we went
    # out of bounds from a node that has one child. The node is not considered a leaf node because it has a child.

    # Note: when we pass a leaf node, we return False from there upwards to the leaf node, but when we backtrack to the leaf node,
    # the next if block potentially could be executed and we can return True from there all the way up to the root because we found a
    # solution. So while we return False from the non-node to the leaf, but if leaf was not 0, we're gonna return True from leaf to the root despite
    # having returned a False from non-node to leaf.
    if not root or root.val == 0:
        return False

    # Second base case
    if not root.left and not root.right:
        return True

    if canReachLeaf(root.left):
        # if there was a leaf node, this return statement or the next one, will be executed all up to the root of the tree.
        return True

    if canReachLeaf(root.right):
        return True

    return False


# T: O(n)
# M: O(h)
def leafPath(root, path) -> bool:
    if not root or root.val == 0:
        return False

    # maintain some kind of solution and keep adding values to it as we're trying search for a solution. But as we found out that we went
    # down a wrong way, we pop from the path(look at the path.pop()).
    path.append(root.val)

    if not root.left and not root.right:
        return True

    # we're not creating a new copy of path variable, we're passing the reference to it to this func call.
    # It works the same in most langs.
    if leafPath(root.left, path):
        return True

    if leafPath(root.right, path):
        return True

    # we have to backtrack. This is only required if we have a global state or the param is a reference type.
    # current path didn't lead to a solution, so pop from path and backtrack(go up). This pop could be recursively get called when we're
    # going upwards(when we're backtracking).
    path.pop()

    return False
