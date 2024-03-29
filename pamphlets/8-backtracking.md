# Section 08 BACKTRACKING

## 23 Tree Maze
Backtracking pattern is based on DFS algo.

In this example(determine if path exists ...) we're gonna apply it to a binary tree not a binary search tree.
In this example, when we found a solution though, we won't try the other paths.

When we see it's a dead end, we backtrack and try another route to reach the goal.

We're recursively trying every single path, it's a brute-force approach. Brute-force is a style of algo where you go through
every single possibility.

Another example: If we're given a binary tree not a BST, to find a value, we need to go through every node(we have to check
both left and right subtrees) This is brute-force. But if it's a BST, we can take advantage of the sorted property and
eliminate up to half the nodes in every step.