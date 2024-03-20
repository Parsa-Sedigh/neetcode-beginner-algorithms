# T: O(n) where n is the size of the tree or number of nodes. We visit every single node once.
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
