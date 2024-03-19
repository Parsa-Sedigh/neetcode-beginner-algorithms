# Section 07 TREES

## 17 BINARY TREE
They're similar to linked lists in the way that we have nodes which have a value.

When a node doesn't have **any** children, we call it a leaf node. 

With binary trees, we're always guaranteed to have leaf nodes. Why? Can't we connect the leaf nodes to for example the root node?
No because unlike linked lists, in binary trees, we're not allowed to have cycles. That's part of the definition of a binary tree.

When two nodes have the same parent, they are called **sibling nodes**.

### Height
A property of a node is it's height. The height of a leaf node is 1. But the height of a 
non-leaf node(where it does have some children) is the number of nodes including itself going down to the **lowest** descendant of the node.
In other words, the height of the node is the longest path going down(including the node itself).

### Depth
Is measure as the path from node itself to the root. So the depth of the root node is 1.

## 18 BINARY SEARCH TREES

19 BST INSERT AND Remove

20 Depth-First Search

21 Breadth-First Search

22 BST Sets and Maps