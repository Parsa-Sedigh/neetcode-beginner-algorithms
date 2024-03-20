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

**So when it comes to inserting and deleting from an arr, it's gonna be O(n) in worst case **whether it's sorted or not**. But that's not true
for BSTs. With BSTs, inserting and deleting can also be O(log(n)).** And that's the main benefit of BSTs.

**The main benefit of BST over sorted arrs is that we can insert and remove in O(log(n)) instead of O(n) (assuming the tree is roughly balanced).**
Inserting is gonna traverse the height of the tree, when tree is roughly balanced, it's gonna traverse log(n) nodes.

When tree is roughly balanced, the height of the tree is roughly log(n).

Note: To find a node in BST, we don't have to go through every node because we know we have the sorted property of BST.
So ideally, we would eliminate half of the remaining possibilities at every level of the BST.

## 19 BST INSERT AND Remove
Note: As we go in one direction, we're essentially traversing a linked list.

In insert and remove, we're expected to insert or remove the node and then return the new subtree to the parent.

### remove
Break it to two cases:
1. node that we wanna remove, either has 0 or 1 child
2. node that we wanna remove, has 2 children

There are two approaches for solving case 2:
1. It's best to replace the node we wanna remove with a leaf node of it's right subtree but which leaf node?
Should we pick the largest val in the leaf level of right subtree or the smallest value? We have to choose 
the smallest val. If we do this, it satisfies the sorted property. Because all the remaining nodes on the right subtree are
greater than the new node that we replaced(since we picked the smallest val in the right subtree). We will use the `minValueNode()` func.
2. We can choose the largest val in the left subtree of the node that we wanna remove and replace it with the node
we wanna remove. Why this works? Since the new val that we picked is less than the node we wanted to remove, so it's also gonna be less than
the right subtree and since the node we chose is largest in the left subtree of the node we wanted to remove, it's gonna be
greater than all of the left subtree, so it's the right choice to keep the sorted property. But we will use the first approach.

![](../img/7-trees/19-1.png)

The BST remove() func in the worst case:
1. find the node to remove
2. find the minimum node in the right subtree. In worst case for this, we could traverse the whole height of the tree which is log(n) if balanced.
3. replace the found minimum with the node we wanna remove
4. remove the found minimum. We could traverse the height of the tree **again**. Note that the minimum could have at most 1 right node(assuming no
duplicates in the tree, but if there was a duplicate, we still would get the child).

So the second time we called remove() (on a different node that we were originally removing), it's gonna be the last time we remove a node, 
because it's gonna be the node with 1 or 0 children.

So the worst case is we traverse the height twice: 2 * O(log(n))

So this was the benefit of BSTs over sorted arrs, we can insert and remove in O(log(n)) instead of O(n).

## 20 Depth-First Search
Inorder: For every node, we went left as far as we can, process it, then we process the parent, then we go right.

Building a BST: We have to insert every value in the BST and an insertion is O(log(n)) for a balanced tree and for n values: O(n * log(n)).

`Time complexity of building the BST: O(n * log(n))`

Building an array out of BST:
- First we have to build the BST -> O(n * log(n))
- traverse the BST to build the output arr in sorted order: O(n) . We do this by using inorder traversal which gives us the nodes in sorted order.

So the time complexity is: O(nlog(n) + n). Any constants are ignored. So: `O(n * log(n))`

So to be given some values that are not sorted and to sort them using a BST and create a sorted arr, it takes O(n log(n)) which is 
similar to some other sorting algos like merge sort and quick sort.

## 21 Breadth-First Search
Level order traversal.

## 22 BST Sets and Maps
### Set
Sets and maps are commonly implemented using BSTs and also with hashsets and hashmaps.

Set is like an arr but the word set implies that there's some other underlying DS being used not an arr. One implementation is BST.

The advantage of having a set implemented with a BST rather than an arr is we can search, insert and remove in `O(log n)`.

### Map


When implemented with BSTs, these are called ordered set or a tree set and ordered maps and tree maps.
![](../img/7-trees/22-1.png)

Java and C++ have native tree maps, but py and js don't have them.