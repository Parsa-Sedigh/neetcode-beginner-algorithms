# T: O(n) where n is the size of the tree or number of nodes. We visit every single node once.
# M: O(h)


# The time complexity of the inorder traversal algorithm is O(n), where n is the number of nodes in the binary tree.
# This is because the algorithm traverses each node exactly once, performing constant time operations at each step.

# The memory complexity of the algorithm depends on the maximum depth of the function call stack during the
# traversal. In the worst-case scenario, where the binary tree is skewed to one side (essentially forming a linked
# list), the depth of the call stack would be equal to the number of nodes in the tree, leading to a memory
# complexity of O(n). However, in a balanced binary tree, the depth of the call stack would be proportional to the
# height of the tree, which is O(log n) for a balanced binary tree. So, the memory complexity can be stated as O(h),
# where h is the height of the binary tree.
def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)



def preorder(root):
    if not root:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)

############ Iterative ###############

# T: O(n)
# M: O(h)
def inorder_iterative(root):
    cur = root

    # Do not add `root` at the stack at the beginning. Since if the tree was empty, we're gonna go inside the while loop and get
    # runtime err.
    stack = []
    res = []

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        # Note: We can't do res.append() BEFORE the next line. Because at this point, cur is None.
        # Since at this point, we traversed all the left subtree, we can add the parent(which is last el )
        cur = stack.pop()
        res.append(cur.val)

        cur = cur.right

    return res

# T: O(n)
# M: O(h) - if the output arr is counted as extra memory, it's O(n)
def preorder_iterative(root):
    cur = root
    stack = []
    res = []

    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)

            cur = cur.left

        cur = stack.pop()

        cur = cur.right

    return res


# T: O(n)
# M: O(h)
def postorder_iterative(root):
    cur = root
    stack = []
    res = []

    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)

            cur = cur.right

        cur = stack.pop()
        cur = cur.left

    res.reverse()

    return res

# T: O(n)
# M: O(h)
def posorder_iterative2(root):
    # Stack to hold nodes to process
    stack = [root]

    # A parallel list of True/False flags that tracks whether a node’s subtrees have been visited.
    visit = [False]
    res = []

    while stack:
        cur, v = stack.pop(), visit.pop()

        if cur:
            if v:
                res.append(cur.val)
            else:
                stack.append(cur)
                visit.append(True)

                stack.append(cur.right)
                visit.append(False)

                stack.append(cur.left)
                visit.append(False)

    return res