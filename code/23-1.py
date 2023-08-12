def canReachLeaf(root):
	# the base case is we reach a null node or we reach a node with the value zero. But we do have another base case which is when
	# we get to a leaf node
	# First base case
	if not root or root.val == 0:
		return False

	# Second base case
	if not root.left and not root.right:
		return True

	if canReachLeaf(root.left):
		return True

	if canReachLeaf(root.right):
		return True

	return False