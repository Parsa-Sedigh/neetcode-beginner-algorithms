## 06 SINGLY LINKED LISTS
### How linked lists are stored in memory?
Linked lists are not stored in memory the same way that we use them as programmers. The ListNodes could be in some 
random order in memory but they're connected via pointers. We can have a mess in memory but as programmers, we're gonna have a clean
order of ListNodes. So this is a difference between linked list and arr. Arrays are stored the same way as 
programmers see them(ordered) but linked lists are not necessarily stored the same way in memory. Look at the img.
![](../img/6-linked-lists/6-1.png)

### Add a new node at the end
Suppose we have a tail pointer which points to the end of the current linked list:
```python
# t: O(1) - assuming we have the tail pointer(if we don't have, it would be O(n), since we need to reach the end)
tail.next = Node
tail = Node # or: tail = tail.next
```

Removing a node:
```python
# head is the prev node that we wanna remove
head.next = head.next.next
```
In most languages, we have GC, so we don't need to take care of de-allocating the removed node. Because there aren't 
any pointers pointing at it.

So this is a benefit compared to arrays. We can remove any element(from beginning or end) in constant time(assuming we have it's prev node).
Because we don't have to shift everything over. But practically, we have to get to the prev element of the node we wanna remove, 
so removing would be O(n) .

## 07 DOUBLY LINKED LISTS

## 08 QUEUES