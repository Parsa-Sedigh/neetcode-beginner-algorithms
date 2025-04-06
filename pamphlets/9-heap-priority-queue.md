## 24 Heap Properties

### Heap / priority queue

Important DS.

Queue: FIFO.

In this DS, we want to order the queue differently. Instead of ordering it by first in first out, we could order it
based on some type
of priority value. For example we add some values to the queue and our queue now is: [7, 3, 9]. Now which value are we
gonna pop first?
Well, it depends on the priority of the values. There's typically two variations of priority queue:

- minimum priority
- maximum priority

In this example, we could prioritize the minimum values first. So if we did it like that, we would first wanna pop the 3
and then pop the 7
and then pop 9. Now this is dynamic meaning as we add values, we might choose to pop a different value than what we
wanted to pop before.
For example let's say the queue is [9]. Now there is only one value and therefore obviously, we would pop 9 when the
pop() function is called,
but let's say we add a smaller value like 4. Now the queue is [9, 4]. Now if the pop() is called, we wanna pop 4 first
and then 9.

With maximum priority -> first pop 9, then 7, then 3.

The reason we have two different names here(heap/priority queue) is kinda the same idea. When we originally had queues,
those queues were
actually implemented with linked lists. So in this case, the relationship between heap and priority queue terms, is
similar: the interface that
we're using is called a priority queue but underneath the hood, that's implemented using a heap. But in this case, a
priority queue is going to
be implemented with a binary heap which is the DS on the left in img.

That heap(binary heap) could either be a min heap or a max heap depending on how we wanna implement our priority queue(
whether we care about
minimums or maximums). Generally it's more common to use a min heap rather than a max heap. The DS on the left of img is
a min heap.

![](../img/24-1.png)

1) structure property
2) order property

At first glance, the DS in the img looks like a binary tree and that's because it is a binary tree, but it's not a
binary search tree. Because
we know in BST, every value in the left subtree is smaller than the root, but in the img, it's not. Actually when you
look at the root node in the
img, it's smaller than every single descendant in the tree. That's gonna be the **order property** that we're gonna talk
about in a minute,
but let's first start with the structure property:

**A binary heap is essentially a binary tree that is considered a complete binary tree.**

A complete binary tree means we have a tree where every single level in the tree is going to be completely full, there's
not gonna be any holes
anywhere except possibly the last level. The last level might have some holes but every other level, but every other
level in the
tree is not gonna have holes.

Another thing about the structure property:

As we add values to the heap, they're added left to right in the last level. Since we want to have a complete binary
tree at any given point in time.

About the order property:

**The whole point about having a heap aka priority queue, is about finding either the minimum or the maximum value
quickly
and easily.** That's
the entire point of having a priority queue.

So for example for the minimum heap, we want the minimum value among all of the values, to be at the root. Because from
the priority queue,
we want to be able to find the minimum easily. By looking at the root, we can do that pretty quickly in `O(1)` (as long
as we're not removing
that root).

Q: So what order property should we give this heap to do that?

A: We should say: recursively for this tree(the min heap), we want every value in the left subtree to be **greater than
or equal to root** and every value in the
right subtree to also be greater than or equal root. That's the only requirement we have. But it's recursive. That means
for the root node of the left subtree,
we also want this. We want every value in it's left and right subtree to be greater than or equal the root(root of the
left subtree). So look at
node 14 and 19 and 16 and ... . This requirement is true for all of them.

**Note:** Technically, in heaps, we're allowed to have duplicates. For example, we have two 19s in the img. So in min
heaps, we don't necessarily need
every value in the left and right subtree to be greater than(and not even equal) the root, it's OK if they're equal as
well. This wasn't true
for binary search trees, but it is true for heaps. In heaps, we could have duplicates.

Note: For a max heap, all the descendants are smaller than or equal to the root. Since we want the overall maximum value
to be at the root of the whole
heap.

---

One of the most interesting things about binary heaps is that while we draw them as binary trees that are connected via
pointers and nodes,
they're actually implemented under the hood using **arrays** and another interesting thing is that we actually don't
start at index 0 for that
array, we essentially don't care about the zeroth index and we'll see why. We put the root node at index 1.

**The root of heap is always gonna be at index 1.**

**Note:** We know the root is at index 1. To get it's left child, we go to index 2, to get it's right child, we go to
index 3. We'll see
what's the pattern behind this and then we'll understand exactly why we use arrays rather than nodes and pointers.

The main reason we skip index 0 is to get the math to work out. What do I mean by math? Well, to get the left child of a
node, we have
a formula. These formulas are only true because we have a complete binary tree(every node is filled except possibly the
last level). These formulas
would not be true for a regular binary tree or regular BST. In addition to the formulas being worked out, that's also
why we can use an array
to represent the heap.

Note: To get to the parent, we divide by two and **round down**.

Next we're gonna talk about how we can insert and remove nodes from a heap, while maintaining the structure and the
order properties, because
those properties are important. Without those properties we don't have a heap anymore.

![](../img/24-2.png)

## 25 Push and Pop

### Push

Inserting into the heap aka pushing into the heap.

Pushing into a min heap:

Let's say we want to push value 17. Well thinking about the structure property, the obvious place we would wanna put it
is next to the
30(right side). We could put it like as the left child of 68(still at the leaf level), but then there's a hole between
30 and 17, **we want
the leaf level to be contiguous**. So now the structure property has been satisfied, what about the order property? Well
remember the heap
in img is a min heap so for every node, we want it's children to be greater than it. So for node with value 17 that we
just inserted,
we want it's parent to be **smaller** than it. So let's compare it's value to the parent. BTW, the new node will be at
index 10 of the array
representation of min heap. Now how do we get the parent of this new node? We know `parent = i / 2`. So parent is at
index 5 which is 26.
In this case, the parent is larger(26) but it should be smaller(note that they are allowed to be equal), so these two
nodes should be
reversed. The smaller one should be the parent. We simply swap the two values in our array(obviously that means that the
tree representation
would also change) and then we would continue the algo. Now **again** we compare the new node(which is now at the level
3), to it's parent - which
now is 19. We want to make sure that the order property is being satisfied. Note that OFC it's satisfied everywhere else
in the tree, but
with this new node, it might not be satisfied. It's parent index is 2. The parent should be smaller but it's not, so
again we want to swap.
So now 17 is at index 2 and 19 is at index 5.

Note: Before we compare 17 to 14, the reason we don't have to compare 17 to it's left child(21) and the whole left
subtree, is because
we already knew 19 which was previous at the position of 17, was valid, it was allowed to be there, because 19 was
smaller than all of the
left subtree. But now we replaced 19 with a value **even** smaller than it, which si 17. Therefore, 17 must also be
smaller than
all the values in it's left subtree. So we don't have to compare it to every single value that's a descendant of it. Now
again compare 17 to 14,
we know 17 should be greater than it's parent and in this case, it is. So the order property is being satisfied. So
we're allowed to stop.
So either we go al the way to the root of the tree or we get to a spot where the order property is being satisfied.

Look at `25-1.py`

Time: Height of the tree. And in this case(heap), we actually know that the tree is always going to be balanced. That's
kinda the point
of having a complete binary tree. So in this case, we can definitively say that the time complexity is going to
be `O(log n)` where `n` is
number of values in our heap aka in our array.

Note: The heap itself is just a dynamic array.

### Pop

Removing from the heap aka popping from the heap

**We don't actually specify a value that we wanna pop because remember our priority queue is about popping the priority
element and we know that
the minimum is gonna be at the root, so that's the one that we're always gonna pop.** It seems simple but actually
popping is more complicated
than pushing(inserting).

If we just wanted to **read** the top element, in other words we just wanted to read what the minimum element is in our
priority queue,
we could just go to index 1 and then return that. But to actually pop it, it's gonna be a bit more complicated, because
we have to maintain
the structure and order properties.

Now after removing that node(obviously the root, because in popping we always remove the root) or that value from the
array,
your first instinct might be to just take the minimum of it's two children and replace it with the removed node. Then we
again replace
the one that went to the root, with minimum of their children and repeat this ... . The order property is being
satisfied, but not the structure
property. Notice the third level in img is not full anymore. We introduced a hole in that level.

So this approach doesn't work. To get pop to work and to maintain the structure and order properties and do it
efficiently, we have to use sorta a
genius technique.

What we actually do is remove the root and replace it with the last value in the array or in other words, the last value
in our tree, which in img
is 30. Because remember that's the way to maintain the order property. So we remove 30 and move it to the root and OFC
under the hood,
that's actually going on in our array. Until now, we have satisfied the structure property but not the order property.
But we can fix that.
Instead of percolating up like we did when we inserted a node, we can do the opposite by taking the current root and
percolating down, because
we don't know that the current root is in the position is should be at. We need the minimum to be in the root. We know
the current root is
probably not the minimum. Now we take the minimum of the two children of current root and we compare it to the current
root(30).
16 is smaller, therefore, we swap them. Now we already know 16 is smaller than all of it's left subtree(not that current
16 is at the root of the tree).
Because it's smaller than 19(it's left child) which is smaller than all of it's children(because of order property).
Remember heaps have a
recursive order property. But we're not done yet, because we need to satisfy that recursive order property. 30 should be
smaller than
all of it's descendants. So again take the minimum of it's two children, it's 19, is 30 smaller than 19? No, swap them.
Now we're done.

Now our min heap is satisfying all the min heap properties(those two).

![](../img/25-1.png)

It's really counter-intuitive that we would do it this way, we would literally just take the last node, move it to the
root and then
percolate down, but **that is the most efficient way to do it**.

Note: The zeroth index is the dummy value

Note: The while loop explained: There's multiple cases when we're at a node:

1. It could have both children
2. it could have just a left child.
3. we don't have any children

**Note:** It's **impossible** for a node to have a right child and not have a left child. Because that doesn't satisfy
our
complete binary tree definition. So we only worry about the cases where we have two children or just a left child or not
any children

Note: We can check that we have a right child with: `2 * i + 1 < len(self.heap)`

There are many ways to write pop method.

`Time:` height of the tree O(h), we know it's a balanced binary tree, so the height is going to be `log n` => `O(log n)`
and this comes from
percolating down.

![](../img/25-2.png)

## 26 Heapify

One of the advantages of heaps over binary search trees is: we can get the min or the max depending on what kind of heap
that we've
implemented, in `O(1)` time(constant time), whereas in BST, you would do it in `O(log n)` because you have to kinda go
all the way left
in the tree.

Another advantage of heaps is how we can build them. We know when we have a BST, you have to insert a node every single
time to build that
BST and the time complexity of that is `O(n logn)`, because we have to do n insertions and to insert each one, takes O(
log n) time.
Now for heaps, you can do it the exact same way, you can keep pushing elements into the heap and it will also
take `O(n logn)` time. But there's
actually a special algo with heaps which is sometimes called **heapify** or just build heap and the idea is that we're
given a list of
values in the format of an array like in the img and they're in no particular order and we can turn them into a heap
that satisfies the
properties of a heap and we can do that in `O(n)` time.

How?

Look at the img, if we're given an array in that format, we see it doesn't even satisfy the structure property because
we know we don't
want to have a real value at zeroth index. So the simple thing to do here since we know these are already in no
particular order, is just
take the zeroth index element and move it to the last position of array.

Now with the current array(moved zeroth element to the end), our heap looks like this:
![](../img/26-1.png)

At this point, we have satisfied the structure property easily, but now we have to satisfy the order property.

**Note:** The order property is recursive. Which means for every single subtree, every node should have a value that's
smaller than all of it's
descendants(for min heap).

Now for every single node, we're gonna check does it have a value that's smaller than all of i's descendants(for min
heap). So we can start at the
bottom nodes(leaf nodes) and then move our way upwards. So we can start at the last node of heap, but when we get to
that level, we know
they don't have any children anyway, so there's no point in doing any kind of comparison. This is true for the leaf
level and potentially some of
the nodes in one to last level(in img, these nodes are 60, 90, 20, 70 and 10). They don't have any children, so we have
nothing to compare them
with anyway. This statement is gonna be true for half of the nodes. So we can actually just skip these nodes if we want
to. I mean, we **could**
start at the end of the array and run the algo to the start of the array, but there's no need too. So to be a little bit
smarter,
we can just skip half of the values. Now how would we do that in terms of code? Well, we can get the number of nodes in
the heap which is not
necessarily the number of nodes in the array because we know we have a dummy value at zeroth index. So we take the
length of array and subtract it
by one to get the actual number of nodes, in this case, 9. Then divide it by 2 and round it down => 4. This leads us to
be at index 4.
So 30 is the first node that actually has children.

If you don't remember a fact like this, it's still OK to still start at the end of the array and go backwards, it
shouldn't change the overall time
complexity.

So we're at 30. Check if 30 is valid: Is it smaller than all of it's children? Yes. So we don't have to do anything.

Notice what we're doing here is the same percolating down algo that we talked about earlier when we were removing nodes.
This is the exact
same thing. What we're doing here, is going through every single node that has children(you can skip the ones without
children or just go through
them as I mentioned above) and percolating down if it can be moved down. Now go to the next one, 40(we're going
backwards).
First does it have two children? Yes. Is the right child smaller than the left child? Yes. Is the right child smaller
than the parent?
Yes. So we swap 40 with the right child(which means swapping them in the array). We already knew the right subtree of
our current position was
a valid heap and the left subtree was also a valid heap and now with the root, we know the entire subtree is a valid
heap. Now we get to 80
and again this algo ... .

When percolating down, if a node doesn't have any children, we don't do anything on that node and we continue to the
next value of arr(backwards).

Note: In heaps, there's an actual array under the hood that's maintaining them.

![](../img/26-2.png)

Look at `25-1.py` `heapify` method.

The heapify algo is similar to pop algo. Only in the heapify(or build heap) is gonna be passed in an input array and
when we have that array,
we're gonna take the zeroth element and move it to the last position of the arr.

Then in

```python
self.heap = arr
```

we're assigning the array to be our heap. We know it(the arr) satisfies the structure property, now it's time to satisfy
the order property ... .

**Q:** Why the heapify algo a linear time algo? Because at first glance, it seems to be an O(n log n) algo because we're
going through pretty much
every node in the tree and having it percolated down, it might be `log n` operation.

**A:** First of all, if we had to take every node and percolate it up, or if we had to take ever node and percolate it
down, which one would we
rather do? Which one seems more efficient? Well, if we're percolating down, then only the root node actually has to go
through the `whole
height` of the tree and then the next level nodes have to go through the `whole height - 1` and other levels going even
smaller distance and we get
more and more nodes as we go down, because remember this is a **complete** binary tree.
But if we're percolating up, it's **worse**. Because at the first level(from bottom), we have a bunch of nodes that have
to go
the whole height of the tree and then we have a smaller number of nodes that have to go `whole height - 1` and ... .

So **percolating down is gonna be more efficient**.

**Note:** Percolating down is `O(log n)` operation.

**Note: Heapify algo is O(n).**

**Note: You can push and pop from heap in O(log n) and you can get the min or max depending on what type of heap you
have in O(1)**

Let's say n is total number of nodes in the tree and let's say we actually had the full binary tree(leaf level is full).
We know that roughly
half of the nodes are gonna be in the last level. For example a full binary tree has 1, 2, 4, 8, ... nodes in each
level.
**The number of nodes in each level = number of all the previous level nodes + 1**.
Let's say we have roughly `n / 2` nodes in the last level. Now for each of these nodes, how much are we gonna have to
percolate them down?
Well remember the last level doesn't need to be percolated at all. So we get `0 * n / 2`. What about the previous level?
That's gonna have half of the nodes that the last level has, so n / 4 nodes, how much are we gonna have to percolate
these down?
One each, so: `1 * n /4`. So till now: `0 * n /2 + 1 * n / 4`.
If we expand that, we get a sum of the one in the img. The number of terms(like 1 * n /4 or 3 * n / 16) that we're gonna
be adding together
is going to be roughly equal to the height of the tree. The sigma in the img is gonna roughly evaluate to `n`. So the
time complexity is indeed `O(n)`.
![](../img/26-3.png)

---

The important thing here just because we can be given some random n elements and then turn that into a heap, doesn't
mean we can actaully
sort all of them in `O(n)`. Because just because we have a heap, if we wanted to turn that heap into a sorted array,
means first we built the heap
in O(n) but then we'd have to pop every single element in the heap. We know popping is still going to be a `O(log n)`
operation, if we have to
for n elements, then it'll take `O(n log n)`. So we can use heaps also to sort values and we can do that also in O(n log
n), just like
binary trees, just like merge sort and the rest. So this is yet another example of sorting.

---

### Downside of heaps

We talked about some of the advantages of heaps over binary search trees:

- we can get the min and max in O(1)
- we can heapify in O(n)

But the downside of heaps is that we can't just search for a random element and then do that in O(log n) like we can
with BSTs. With a heap,
suppose we're looking for 30. We get to the root, it's 14 not 30. Now we know all values in both left and right subtrees
are greater than 14.
So the 30 could be in both subtrees! We don't know in which subtree it is. We haven't narrowed it down. So to search for
an element,
we'd have to go through every single node in the tree which is gonna be `O(n)`, but with binary search trees
it's `O(log n)`.

So binary heaps are not good for searching, but that's ok, because they're not intended for that, they're intended to
get the priority element
which is either the min or the max.

---

In interviews, you actually have to use a heap more often than you have to use binary search tree. At least when we're
talking about a built-in
DS, where the DS is a part of the solution. BST problems are also common but it's usually you're implementing a part of
the BST, you're
searching for sth, you're calculating sth, but when it comes to problems where you actually have to use a DS as like a *
*utility DS**,
it's pretty rare that you end up actually needing BSTs, it's more often that you need a heap, because it's more often
that you need a minimum or
a maximum value you need to continue doing that.

There are a ton of algos where heaps are really important.

**Note:** In heapq lib, when you want the heap to have custom elements instead of just integers, add them as a tuple. For example:
```pycon
heapq.heappush(heap, (freq, num))
```

heapq lib is smart that sort the heap based on `freq`(the first el of tuple).