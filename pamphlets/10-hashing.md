# Section 10 HASHING

## 27 Hash Usage
### hash sets/maps
In hashset we only have a set of keys, but in hashmap, each key is gonna map to some value.

Unlike a list, there can't be any duplicates in hash sets / maps.

The key is used to sort the binary search tree and is used to access values from hashset and hashmap.

Note: We can remove values in O(1).

### Tree map vs hashmap
When we have a map, we wanna:
- insert
- remove
- search

In tree maps is O(log n) which is better than inserting into a sorted arr which in worst case would be O(n) .

Also in treemaps(we know they're ordered), we can iterate through them in sorted order(inorder traversal) in O(n).

Note: In a hashmap, when we say it's insert op is O(1), we're not telling the worst case! Even though we're writing it as big O which means
worst case. **When we say hashmaps have O(1) for these three operations, it's actually the average case time complexity.** But the vast majority
of the time, people still assume that it is the worst case time complexity, so we write it as O(1).

**So the three first ops for hashmaps have average case of O(1). But in worst case for hashmaps, these three ops could be O(n) depending on how
you implement the hashmap.**

Now **the downside of hashmaps is that they don't maintain any ordering.** As a result, if you wanna iterate through all the keys of the hashmap
in a specific order, you can't do it in O(n), you have to take all the keys and then sort them which depending on what sorting algo you use,
it typically would be O(n log n) .

The positive points of hashmap beat the negative point which is not having an order and worse time when iterating the elements in an ordered manner, than the
tree map. Especially if we don't need to traverse the hashmap in order, then they're really important.
![](../img/10-hashing/27-1.png)

Note: Hashmaps can not contain duplicate keys and that's the exact same thing with binary search trees. So a treemap is also not allowed to
have duplicates.

![](../img/10-hashing/27-2.png)
- Time: O(n)
- Space: O(n)

## 28 Hash Implementation
Under the hood, a hashmap is actually implemented with an array. The index of the arr will be mapped to the key-value pair. Note that just because
we have an empty hashmap, does not mean the size of the underlying arr is 0. Even an empty hashmap is gonna have an arr with a size like the arr
has 2 elements that their key-value pair is empty like null(some default value).

The key could be anything that can be converted into the index of the underlying arr. The way we do this is called **hashing**. We're gonna have
a hashing func which is gonna take the key and convert it into an integer and when we have that mapping, we use that int as the index of the underlying arr.
That's how we decide where to put that key-value pair in the underlying arr.

So the underlying arr is an arr of objects where the obj itself is a key-value pair and we have an index for each(since it's an arr).

We can take any integer, no matter how big it is, as long as it's positive and mod it by the size of our underlying arr.

Mod: For example when we have 25 % 2, it means we're dividing 25 by 2 and we're getting the **remainder** that's left.

Now when we mod by the **length of the arr**, no matter what integer we're modding by, you're always gonna get a valid index for the arr.

When we wanna get a value of a key, for example key is "Alice", we would use our hashing func, convert Alice to an integer, like 25,
mod that by the size of the underlying arr, then we get for example 1 which is the index of the arr that at that index, we have a key-value
pair of `Alice: NYC`.

But there are a few problems. Like **the collision problem which happens with all the hashing algos.** It's sth you can't entirely avoid.
There are ways that we can use to **1-minimize collisions and 2-workaround them**. But we can't entirely get rid of them. Hashing collisions always happen.

**Collision:** The index of the underlying arr that we wanna insert sth, is already taken.

First let's see how we can minimize collisions?

If our hashmap for example is half full, we have a 50-50 chance of having a collision or getting a position that's empty.
To minimize collision, typically we keep track of the size of the underlying arr and also how many keys are inserted into the underlying arr.
Typically, when the underlying arr is half-full, we resize the underlying arr and resizing the arr works exactly the same as when we did it with
dynamic arrays. Meaning we take the curr size and roughly double it. Everytime we insert sth, after the insertion, we would check if the 
hashmap is half-full, at that point we would've resize the underlying arr.

But after the resizing there's a problem, because now the size is different so when we wanna get a key, we could go to the wrong index. because we're
moding by a different number. For example when we were inserted a key, we would do: `<the int result by hashing func>%2` , but now we're doing:
`<same int resulted by hashing func>%5` .

So when we resize the underlying arr, we can't just leave the values(key-value pairs) where they previously where. Because the size changed,
therefore the index using our hashing func might have also changed.

So when we resize, we take every single key-value that's already in the hashmap, we recompute the hash of it using the new size and then
move it to where it should now be.

The process of increasing the arr size and then moving all the elements to their new position is called **rehashing** the underlying arr.

Since we're doing it when the size is half-full and we're doubling it every time it's half-full, it's still relatively efficient(in the
average case) because it's gonna be infrequent that we have to do rehashing. But overall it's a pretty expensive op, because we're gonna have to go through
every key-value that's in our hashmap.

By rehashing, the chance of collision have decreased because we have a bunch more empty positions in the underlying arr. 

**So we minimize the chance of a collision using rehashing(increasing the size of the underlying arr and move the elements to their new position).**

There is another problem: There are cases where even though the hashmap is not even half-full, the index that we wanna insert the new key-value pair
is already taken(collision). So now we should look at the **workaround** of collisions. Note that we could resize the arr in this case as well and that
would decrease the chance of collision, but it still might end up happening as well. So we need a different way(workaround) of handling collisions.
There are multiple ways of doing that:
1. At every index of underlying arr, instead of just storing a single key-value pair, we store a linked list of pairs. So we could have multiple pairs
occupying the same index of underlying arr. The downside of this is we have to maintain the memory and pointers of all that and also when we 
run the `get` op of hashmap and we find out we need to go to an index, we have to traverse through the entire linked list in worst case.
This linked list approach is commonly referred to as **chaining**
2. Another approach is **open addressing**. It's called that because we kinda loosely define the index that a key should go. For example, even though
we computed the index 1 for a key, we don't have to put it at that index in the underlying arr because it's already occupied. In this case,
we try the next index. Now in this approach, when we run `get` op on this key which was put at index 2 for example, first as always we compute the hash,
we would again get 1, we would see well at that index, we don't have the key we wanna get. So if that key exists, maybe it's at the next index, in other
words, maybe we open-addressed it. So try the next index. Then we would find it. Another example is we wanna `get` a key that actually doesn't exist in
the hashmap, in this case, we go to an index, it's not there, we say: maybe we open-addressed it, so try next index, it's again not there and ... we go
to next index until we see an empty index. At this point, we know we can stop. We don't have to search to get the key through the entire arr.
Why we would stop there? Because if that key did exist, it would be at this spot, but this spot is empty. So that key definitely doesn't exist. 
If we don't stop, it wouldn't be an efficient algo, it would be O(n). Here, we would increment the index and mod it by capacity and then again check
if we arrived to the key we want and ... . If we arrive to an empty spot, it means we can stop.
Note: This is a naive way of doing open-addressing, because we're just trying the next available index every single time. The downside of this approach
is we're gonna **cluster** the hashmap potentially. If we have a big hashmap and we get a lot of collisions, all the keys are gonna be stored
close to each other. So there are better ways of doing open-addressing. Like instead of just going one index further to insert(in case of collision),
maybe we go to index^2.

Ways of working around collisions:
- chaining
- open addressing

There are more optimal ways of handling that.

Note: When we maintain the size of the underlying arr, it's more optimal for the size to be a prime number. For math reasons, that ends up
resulting in less collisions for the hashmaps. So when resizing, we double it to be the next prime number. Like if the size is 17,
we roughly double it to be the next prime number which is 37.

![](../img/10-hashing/28-1.png)

To minimize the collision:
- increase the size to minimize collision(the size is better to be a prime num)
- Having some kind of intelligent hash() func also minimizes the collisions. 
- Also having the size to be prime minimizes collisions.

Q: Why insert, remove and search runs in O(1) on average?