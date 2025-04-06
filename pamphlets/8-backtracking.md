# Section 08 BACKTRACKING

## 23 Tree Maze

Backtracking pattern is based on DFS algo.

In this example(determine if path exists ...) we're gonna apply it to a binary tree not a binary search tree.
In this example, when we found a solution though, we won't try the other paths.

When we see it's a dead end, we backtrack and try another route to reach the goal.

We're recursively trying every single path, it's a brute-force approach. Brute-force is a style of algo where you go
through
every single possibility.

Another example: If we're given a binary tree not a BST, to find a value, we need to go through every node(we have to
check
both left and right subtrees) This is brute-force. But if it's a BST, we can take advantage of the sorted property and
eliminate up to half the nodes in every step.

Note: The backtracking phase where we reset some state to it's previous step like popping from the arr, is only required
for:

- global states(outer params or variables of the current nested funcs)
- current local params of the nested func that are **reference types** like arrays or objects or ...

Why the primitive types that are local params do not need to be reset? Because at each func call in the call stack, we
have
the previous state of them, but the reference types are mutated, so we need to reset them.