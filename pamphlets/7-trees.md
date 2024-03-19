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
A special type of binary trees. BSTs have a sorted property(not like literally sorted for example with arrs) which allows us to use them
similar to how we used a sorted arr, especially when we're doing binary search algo which is sorta why these are called binary search trees.

What is that sorted property? For every single node in the tree, every single node in the left subtree has to be less than the root val and
every single node in the right subtree has to be greater than the root val. Also, generally speaking, **BST do not contain duplicate vals**. So we
don't have to worry about that edge case.

### Why?
Why do we care about having a sorted property with this DS? What does it achieve for us?

Pretty much exactly the same thing as having a sorted arr. With a sorted arr, when we need to search for a val, we can do it in O(log(n)) with
binary search. But if the arr was not sorted, we have to look at every el, so it would be O(n). The exact same thing is true for BST. If it didn't
have the sorted property, we would have to look at every single node to find the target. 
But since BST is sorted, we can use binary search.

So if the input is sorted, we can search for the el more efficiently in O(log(n)) instead of O(n).

Note: Even though this DS has two branches at each step, **to search in a BST, is actually one-branch recursion**. Because when we get to a node,
we do our comparison with target and we only go in one direction. There's no need to go both directions in BSTs, that's the efficient part.

The time complexity of search in BST is: O(log(n)), just like binary search algo. But it's only gonna be O(log(n)) if we have a
BST that's roughly balanced. Because our **assumption** is when we get to a node and we choose either to go left or right, **we're
eliminating half of the remaining possibilities every time**.

Balanced means: For every single subtree including the root tree, the heights of left and right subtrees are roughly equal meaning that 
they differ maybe by 1. That would be a perfectly balanced tree.

If we don't have a balanced tree, like when each node has only a right child, we essentially have a linked list. While we still have a BST, meaning
we have a sorted property, we can't eliminate half of the remaining possibilities every time, because we actually can't even jump around.
So if the BST is not balanced, the BST search algo in worst case would be O(n). But the reason we have BSTs is to have balanced BSTs.

**Technically, the time complexity of running search on BST is `O(h)` where h is the height of the tree because for an inbalanced BST,
the height would be `n` because we just have a linked list, but for a balanced tree, the height would be `log(n)`.**

Q: Why do we need BSTs if we can already have sorted arrs? We can have sorted arrs whcih we can run binary search on, we can already search
for val in O(log(n)). So why another DSA?

A: The downside of sorted arrs is when we wanna add or remove values to the arr and keep the sorted property. We know removing from an arr
in worst case is O(n) because even if we can find the val really quickly(O(log(n))), we still have to maybe shift every single el to the left
and if we wanna add a val, in worst case, we have to shift all of elements by one to the right.

**So when it comes to isnerting and deleting from an arr, it's gonna be O(n) in worst case **whether it's sorted or not**. But that's not true
for BSTs. With BSTs, inserting and deleting can also be O(log(n)).** And that's the main benefit of BSTs.

19 BST INSERT AND Remove

20 Depth-First Search

21 Breadth-First Search

22 BST Sets and Maps