from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# T: O()
# Although we have nested loop, it won't make it O(n^2). We only traverse each node once.
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