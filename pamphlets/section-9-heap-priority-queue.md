## 24 Heap Properties
### Heap / priority queue
Important DS.

Queue: FIFO.

In this DS, we want to order the queue differently. Instead of ordering it by first in first out, we could order it based on some type
of priority value. For example we add some values to the queue and our queue now is: [7, 3, 9]. Now which value are we gonna pop first?
Well, it depends on the priority of the values. There's typically two variations of priority queue:
- minimum priority
- maximum priority

In this example, we could prioritize the minimum values first. So if we did it like that, we would first wanna pop the 3 and then pop the 7
and then pop 9. Now this is dynamic meaning as we add values, we might choose to pop a different value than what we wanted to pop before.
For example let's say the queue is [9]. Now there is only one value and therefore obviously, we would pop 9 when the pop() function is called,
but let's say we add a smaller value like 4. Now the queue is [9, 4]. Now if the pop() is called, we wanna pop 4 first and then 9.

With maximum priority -> first pop 9, then 7, then 3.

The reason we have two different names here(heap/priority queue) is kinda the same idea. When we originally had queues, those queues were
actually implemented with linked lists. So in this case, the relationship between heap and priority queue terms, is similar: the interface that
we're using is called a priority queue but underneath the hood, that's implemented using a heap. But in this case, a priority queue is going to
be implemented with a binary heap which is the DS on the left in img.

That heap(binary heap) could either be a min heap or a max heap depending on how we wanna implement our priority queue(whether we care about
minimums or maximums). Generally it's more common to use a min heap rather than a max heap. The DS on the left of img is a min heap.

![](../img/24-1.png)

1) structure property
2) order property

At first glance, the DS in the img looks like a binary tree and that's because it is a binary tree, but it's not a binary search tree. Because
we know in BST, every value in the left subtree is smaller than the root, but in the img, it's not. Actually when you look at the root node in the
img, it's smaller than every single descendant in the tree. That's gonna be the **order property** that we're gonna talk about in a minute,
but let's first start with the structure property:

A binary heap is essentially a binary tree that is considered a complete binary tree.

A complete binary tree means we have a tree where every single level in the tree is going to be completely full, there's not gonna be any holes
anywhere except possibly the last level. The last level might have some holes but every other level, but every other level in the
tree is not gonna have holes.

Another thing about the structure property:

As we add values to the heap, they're added left to right in the last level. Since we want to have a complete binary tree at any given point in time.

About the order property:

The whole point about having a heap aka priority queue, is about finding either the minimum or the maximum value quickly and easily. That's
the entire point of having a priority queue.

So for example for the minimum heap, we want the minimum value among all of the values, to be at the root. Because from the priority queue,
we want to be able to find the minimum easily. By looking at the root, we can do that pretty quickly in `O(1)` (as long as we're not removing
that root).

Q: So what order property should we give this heap to do that?

A: We should say: recursively for this tree(the min heap), we want every value in the left subtree to be **greater than or equal to root** and every value in the
right subtree to also be greater than or equal root. That's the only requirement we have. But it's recursive. That means for the root node of the left subtree,
we also want this. We want every value in it's left and right subtree to be greater than or equal the root(root of the left subtree). So look at
node 14 and 19 and 16 and ... . This requirement is true for all of them.

**Note:** Technically, in heaps, we're allowed to have duplicates. For example, we have two 19s in the img. So in min heaps, we don't necessarily need
every value in the left and right subtree to be greater than(and not even equal) the root, it's OK if they're equal as well. This wasn't true
for binary search trees, but it is true for heaps. In heaps, we could have duplicates.

Note: For a max heap, all the descendants are smaller than or equal to the root. Since we want the overall maximum value to be at the root of the whole
heap.

---

One of the most interesting things about binary heaps is that while we draw them as binary trees that are connected via pointers and nodes,
they're actually implemented under the hood using **arrays** and another interesting thing is that we actually don't start at index 0 for that
array, we essentially don't care about the zeroth index and we'll see why. We put the root node at index 1.

**The root of heap is always gonna be at index 1.**

**Note:** We know the root is at index 1. To get it's left child, we go to index 2, to get it's right child, we go to index 3. We'll see 
what's the pattern behind this and then we'll understand exactly why we use arrays rather than nodes and pointers.

The main reason we skip index 0 is to get the math to work out. What do I mean by math? Well, to get the left child of a node, we have
a formula. These formulas are only true because we have a complete binary tree(every node is filled except possibly the last level). These formulas
would not be true for a regular binary tree or regular BST. In addition to the formulas being worked out, that's also why we can use an array
to represent the heap.

Note: To get to the parent, we divide by two and we **round down**.

Next we're gonna talk about how we can insert and remove nodes from a heap, while maintaining the structure and the order properties, because
those properties are important. Without those properties we don't have a heap anymore.

![](../img/24-2.png)

## 25 Push and Pop
