from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# T: O(n)
# M: O(n)

# Where n is total number of nodes

# Although we have nested loop, it won't make it O(n^2). We only traverse each node once.
# The time complexity of this algorithm is O(n), where n is the number of nodes in the binary tree. This is because
# the algorithm traverses each node in the tree exactly once, visiting each node and performing
# constant-time operations (enqueueing and dequeueing from the queue) for each node.

# The space complexity of this algorithm is also O(n) in the worst case. In the worst case, when the tree is a complete
# binary tree, the number of nodes at the deepest level would be roughly half of the total number of nodes(n/2), resulting in
# a queue of size O(n/2) which simplifies to O(n).
def bfs(root):
    queue = deque()

    if root:
        # add to the right
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level: ", level)

        for i in range(len(queue)):
            # pop from the opposite side of pushing.
            curr = queue.popleft()
            print(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        level += 1