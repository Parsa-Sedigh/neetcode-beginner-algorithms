## 17 BINARY TREE

## 18 BINARY SEARCH TREES
A special type of binary tree which is called a binary search tree(BST).

BSTs are pretty much exactly like binary trees except they have a certain sorted property to them.

They're not literally sorted like an array would be but they have a sorted property which allows us to use them similar to how we use
a sorted array, especially when we were doing that binary search algorithm which is why these are called binray search trees.

What is that sorted property?

For every single node in the tree, the guarantee of BST is that **every single node in the left subtree has to be less than the root value and
every single node in the right subtree has to be greater than the root value.**

What about the case where there's equal values? 

Generally, BSTs do not contain duplicates, so we don't have to worry about that case.

Q: Why do we care about having a sorted property with this DS? What does it achieve? 

A: Pretty much exactly the same thing as having a sorted array. With a sorted array, when we need to search for a value, we can do it
in `log n` time. If the array was not sorted, we would have to look at every individual element, so we would have to search for the
value that we're looking for in O(n) time, but with sorting, we can do it more efficiently(O(log n)). The exact same thing is true for
BSTs. If it didn't have a sorted property, we would have to look at every single node to find the target. But with the sorted property, we don't.
We can follow the same logic as binary search.

If the target is greater than current node, we're gonna go to the right subtree(so we're doing binary search). So we eliminated the current node and
all the nodes on the left subtree and ... . So by doing a single comparison, we eliminate roughly half of the possibilities. We do this
comparison for the next node and ... .

Since binary trees are recursive in nature, meaning a subtree has the exact same structure as the entire tree, we can use recursive algo to traverse it
and search for values.

Even though this DS has 2 branches(left and right tree), to search along a binary, it's actually one branch recursion. The reason is when we get
to a node, we do our comparison based on whatever the target value happens to be and **we only go in one direction**, there's no need to
search in both branches with binary search trees, that's the efficient part.

**search in BST:**
```python
def search(root, target):
    if not root:
        return False

    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
```
Time complexity: `O(logn)` ,like the binary search. It's only gonna be `logn` if we have a binary tree that's roughly balanced, because our
**assumption** is when we get to a node and we choose either to go left or right, as we do that, **we're eliminating half of the remaining possibilities
every single time**. But we can only do that if the tree is roughly balanced.

Balanced means for every single subtree including the root tree, the heights of the left and right subtrees are roughly equal, meaning that they differ
maybe by one. That's a balanced tree.

When we don't have a balanced tree, we kinda have a linked list. But yeah it still has that sorted property. But the way our binary search is gonna run
is it can't eliminate half of the remaining possibilities every single time.

So if the BST is not balanced, the search algo in the worst case would be `O(n)`. But the reason we have BSTs is to have balanced BSTs and it's
usually assumed that if you're working with a BST, you do have a balanced BST.

In terms of technicality, the time complexity of running search is O(h) where is the height of the tree. Because for an inbalanced BST, the
height would be `n`, because we just have a list of nodes one after another in an inbalanced way, but for a balanced BST, the height would be
`logn`, for similar reasons we talked especially when it comes to merge sort since in every level of BST, the number of nodes are being multiplied
by 2, so then the **height** of the tree would be `logn`.

Q: Why do we have BSTs if we can already have sorted arrays?

If we already have sorted arrays which we can run binary search on, we can already search for values in `logn` time. So why create all this
complexity to create a new DS just to achieve the exact same thing?

Well, the downside of having sorted arrays is if you want to add values to the array and remove values from the array and keep the sorted
property of that, we know removing from the array in worst case is gonna be O(n) because even if we can find the value quickly, we still have
to then maybe shift every single value in the array and if we want to add a value, maybe we would have to shift all of the array(like adding
a value at the beginning of the array, we have to shift all the elements one index forward).

So when it comes to inserting and deleting from an array, it's always gonna be O(n), regardless of it's sorted or not, but this is not true for
BSTs. With BSTs, inserting and deleting can also be `log(n)` and that's the main benefit of BSTs over sorted arrays.

## 19 BST INSERT AND Remove

## 20 Depth-First Search

## 21 Breadth-First Search

## 22 BST Sets and Maps