## 06 SINGLY LINKED LISTS

### How linked lists are stored in memory?

Linked lists are not stored in memory the same way that we use them as programmers. The ListNodes could be in some
random order in memory but they're connected via pointers. We can have a mess in memory but as programmers, we're gonna
have a clean
order of ListNodes. So this is a difference between linked list and arr. Arrays are stored the same way as
programmers see them(ordered) but linked lists are not necessarily stored the same way in memory. Look at the img.
![](../img/6-linked-lists/6-1.png)

### Add a new node at the end

Suppose we have a tail pointer which points to the end of the current linked list:

```python
# t: O(1) - assuming we have the tail pointer(if we don't have, it would be O(n), since we need to reach the end)
tail.next = Node
tail = Node  # or: tail = tail.next
```

Removing a node:

```python
# head is the prev node that we wanna remove
head.next = head.next.next
```

In most languages, we have GC, so we don't need to take care of de-allocating the removed node. Because there aren't
any pointers pointing at it.

So this is a benefit compared to arrays. We can remove any element(from beginning or end) in constant time(assuming we
have it's prev node).
Because we don't have to shift everything over. But practically, we have to get to the prev element of the node we wanna
remove,
so removing would be O(n) .
![](../img/6-linked-lists/6-2.png)

## 07 DOUBLY LINKED LISTS

- Insert at end: O(1)
- remove at end: O(1)

**The above, satisfies the requirements of a stack DS. That means that stacks can also be implemented with linked lists,
just like they can be with arrays.
But it's lot less common to implement stacks using linked lists. Because with dynamic arrs, we can also access any
arbitrary element of the arr
in O(1). This is a downside of linked lists(whether singly or doubly). Because we can't access arbitrary nodes in linked
lists.
That means to access a random element of linked list -> O(n)**

**So it's better to use a dynamic arr instead of linked list to create stack.**

Insert and remove at the middle of linked list is O(1). Because unlike arrs, we don't have to shift all the remaining
nodes over by one.
We just manipulate a couple of pointers. But the caveat is to remove or insert any node in the middle, first we have to
arrive at that node to get
a pointer to that node. We have to start at the beginning and iterating until we arrive to the node.

So while the insertion and removing themselves in linked lists are O(1), we have to iterate through the linked list
until we arrive to that node,
so in most cases it's O(n).

So linked lists do have a slight benefit compared to arrays, but arrays are much more useful. Because we can access the
ith element in O(1) in arrs.
![](../img/6-linked-lists/7-1.png)

Being able to access ith element of arr in in O(1), is more important than a insert/remove middle of O(1) (with caveat
of iterating until that node which
is O(n)) in linked lists(most of the time those ops in linked lists are O(n) not O(1)!!!).

## 08 QUEUES

- enqueue: Pushing to the end of the queue
- dequeue: Removing from the start of the queue(that's why queue is FIFO)

We wanna add to the end of the queue and remove from beginning in O(1). We know we can't do that with arrs, because if
you remove from beginning of the arr, then we have to take all other els and shift them to the left by one, that's O(n). But with linked lists, we
can achieve this in O(1).

**Using linked lists to implement queues**:

- enqueue: O(1)
- dequeue: O(1)

Note: Technically we can implement queues with arrs but it can get complex.

### Dummy node technique

With this technique, we add one or two(in doubly linked list) dummy nodes to our overall linked list. The dummy head and
dummy tail.
The dummy tail points to the first real node of our linked list and the dummy tail points to the last real node.

So in order to get the first real node, we should say: self.head.next

And in order to get the last real node: self.tail.prev