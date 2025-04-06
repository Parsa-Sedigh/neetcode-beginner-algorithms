## 23 Tree Maze

The backtracking algorithm pattern is based on the DFS.

Q: Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeroes.(This question is
about regular
binary tree not BST)

A: We're asked to determine if a path exists from the root to leaf node, but the restriction is it may not contain any
zeroes.
Look at `23-1.py`.

First thing to verify is that the root shouldn't be zero. Because if the root node is zero, there won't exist any paths
from the root to any of the
leafs that doesn't contain a zero.

The solution is to use backtracking. Because we try one possibility and if it was not a good result, now we go back up(
backtrack). The idea is similar to
going through a maze. We try every path until we hit a dead end which in that case, we backtrack and we try another
route to reach the end.
So we're recursively trying every single path. It's kinda a brute-force approach.

If we arrived to the leaf node and we didn't see a zero, we return true to the parent and then the parent knows since we
already found
the solution in that subtree which returned true, we did find the path, so there's no need to look in the other subtree.
From there,
we again return true up to the parent and again ... until the root which returns true at the end of the function.

Another example is we know in BSTs to find a value, we can take advantage of the sorted order property of the BST. So at
each step, we don't consider
one subtree. But if we were given a binary tree, not a BST, then we have to check both the left and subtree at each
step, so we have to kinda
brute-force it in that case.

So in backtracking, we have to go through every possibility. When you go through a maze, you have no idea which path
actually leads to the end.

Q: Find the sum of the path that doesn't have any zeroes from root to leaf.

A: Look at 23-2.py

![](../img/23-1.png)

Time complexity for both: **O(n)**

In backtracking, usually the time complexity is O(n) . Because backtracking usually is a brute-force algorithm. In worst
case, backtracking
runs over all possibilities.

Note: In canReachLeaf and leafPath funcs, T is O(h) not O(2^n) (and I think not even O(n), since the tree can be
balanced).