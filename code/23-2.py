def leafPathSum(root, path):
	# when we pass a leaf node, we return False from there upwards to the leaf node, but when we backtrack to the leaf node,
	# the next if block potentially could be executed and we can return True from there all the way up to the root because we found a
	# solution. So while we return False from the non-node to the leaf, but if leaf was not 0, we're gonna return True from leaf to the root despite
	# having returned a False from non-node to leaf.
	if not root or root.val == 0:
		return False

	# maintain some kind of solution and keep adding values to it as we're trying search for a solution. But as we found out that we went
	# down a wrong way, we pop from the path(look at the path.pop()).
	path.append(root.val)

	if not root.left and not root.right:
		return True

	if leafPathSum(root.left, path):
		return True

	if leafPathSum(root.right, path):
		return True

	# current path didn't lead to a solution, so pop from path and backtrack(go up). This pop could be recursively get called when we're
	# going upwards(when we're backtracking).
	path.pop()

	return False