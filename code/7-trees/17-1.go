package __trees

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func search(root *TreeNode, target int) bool{
	if target > root.Val {
		return search(root.Right, target)
	} else if target < root.Val {
		return search(root.Left, target)
	}

	return true
}
