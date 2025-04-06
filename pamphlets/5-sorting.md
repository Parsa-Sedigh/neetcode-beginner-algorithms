Sorting are usually applied to arrays but you can apply it to other DSs including linked lists and ... .


## 11 INSERTION SORT
We consider any array of one element, sorted. So first element is sorted, the next sub-problem is to sort the first two
values.
Then first three values and ... .

So in this algo, the first val is sorted, then the first two vals is sorted, then first three vals is sorted and ... .
The way this algo works, is for each val, we're gonna **inserting** it in the correct order into the sorted portion of the list.

Since we're doing it with sub-problems, we could solve this using recursion, but it's not useful in this case. We're
gonna solve it with
iterative approach.

We start at the second element, because we know the first element is already sorted. Our goal is to figure out where to
put the current element
that we're at? **(previous values are already sorted)**

**Note: If the current element is greater than the previous one, we don't need to compare it to the smaller values in
the already sorted subarray.**
Because the subarray is already sorted. So if current is greater than prev, OFC it's gonna be greater than any value to
the left of the prev. Because
every value to the left of prev is less than or equal to prev(they are already sorted).

It's called insertion sort because we're taking one value(curr) and inserting it into a sorted array(prev values).

`j + 1` is current element and `j` is previous element(which is in the sorted subarray).

As long as we have a way to compare two values like characters(like sorting based on alphabetical order), we can sort
them. Maybe sorting words as well,
based on their first character.

---

Time Complexity:

Best Case: O(n)

This occurs when the array is already sorted. The algorithm only needs to make one comparison per element.

Average Case: O(n^2)

This assumes that elements are inserted in a random order. On average, each element has to be compared with half of the
already sorted elements.

Worst Case: O(n^2)

This occurs when the array is sorted in reverse order. Each new element has to be compared with all the already sorted
elements.

Space Complexity: O(1)

Insertion sort is an in-place sorting algorithm, meaning it requires only a constant amount of additional memory space
besides the input array.

### Stable vs unstable

The difference of a stable and unstable sorting algo, is let's say we have 7, 3, 7 as input. The sorted result is: 3, 7,

The stable sorting algo would put the first 7 to also appear before the second 7 again in the result.
**It preserves the original relative order of the elements that are equal.**

In other words, **the stable sorting algo will preserve the original order when there's a tie.**

**Unstable sorting might preserve the original order of equal elements, but there's no guarantee.**

Insertion sort is stable.

**It's preferred to keep an algo stable, if you can.**

### Time and space

When we have an array as the input that's already sorted, when we run insertion sort, the inner while loop won't execute
at all and we only
iterate through the array. So time is `O(n)`.

So just having a loop in an algo doesnt mean it's necessarily gonna execute in all times.

So **the best case time complexity(which would occur if the input is already sorted in this algo) is: n**. We don't use
O() here because
it's not used with the best case, it's for worst case.

Worst case: Occurs when input is in reverse order(based on what order we wanna sort). In the worst case, for every
single value that we
iterate, the inner while loop would have to execute the maximum number of times until that value shifted all the way to
the left.
But it's **not** O(n^2). Because for input of size 4, it's not n^2 because the while loop doesn't loop 4 times for each
element.
It loops: 1 time(for the second element, we're skipping the first el), 2 times for the third element and 3 times for the
forth element.
So it doen't loop 4 times per element. So we have: 2 + 3 loops for the while loop instead of 4^2 which is 4 + 4 + 4 + 4.

But remember we just want an approximation and that's enough for us when we're doing big O time complexity.

Note: When you have two nested loops it's usually correct.

Note: 1 + 2 + 3 + 4 is bounded by 4 + 4 + 4 + 4(n^2). For proof, look at the vid. Basically it's half the size of n^2(
4 + 4 + 4 + 4), so we can consider
it as n^2 because 1/2 * n^2(n is input), is considered O(n^2).

- stable
- `worst: O(n^2)`
- `best: O(n)`

## 12 MERGE SORT

It's common because it's efficient, since we're splitting it into halfs and it does make things more efficient.

The main idea is to take the input arr and split it into two approximately equal halves and then for those halfs, split
them into two approximately
equal halfs and ... continue to split each sub array until we can't split them anymore, which would mean we have
individual elements left to sort.

We break the original problem into sub-problems.

This algo is a 2-branch recursion because we're splitting the arrays into halfs.

**Divide and conquer: take the original problem and divide it into sub-problems and then solving those sub-problems
before solving the original problem.**

When merging two sorted arrays into a third array, we need 3 pointers:

- a pointer for the first arr
- a pointer for the second arr
- a pointer for the result array

![](../img/5-sorting/12-1.png)

When we merge() the left and right halfs, we do need to create extra memory.

### Time and space

Starting with an array of length n, how many times can we split it by half? In other words, how many levels are there to
this recursion?

It's the same number of times where we can take `n` and divide it by 2. Note that when n = 1, we hit our base case. So
what's the math
formula for how many times we can take `n` and divide it by 2 until it's equal to 1? Well if we were starting at n=1 and
then multiplying
it by 2 every single time, that would be `O(2^n)`, but we're doing the reverse of that. We're dividing it by n. So what
we're asking is we have
n and we wanna divide it by 2 and then divide it by 2 and ... , so sth like: n / (2 * 2 * 2 ...) , so it's:

`n / 2^x` where x is the number of times we're gonna divide n by 2. Now we know we wanna keep dividing it by 2 until we
hit the base case:
`n/2^x = 1`, now by doing some algebra, we have: `n = 2^x`. We care about x, that's how many levels are going to be in
this merge sort algo.
We can take the log of both sides of the equation. We use log base 2 of n and by doing some math, `x = log base 2 of n`.

So how many times we can divide n by 2 until n = 1?

**The log base 2 of n is how many times we can divide it by 2 until it's equal to 1.**

Watch the video from 13:30 to 16:00 to learn the math behind log base 2 of n.

In logarithm, if the base is 2, it's omitted. Log base 2 of n is the number of steps that we're going to have to divide
n by 2 until it's 1.
But what's the time complexity of **each step** of this algo? It's O(n). It has to do with the merge() step. We're gonna
do O(n) in every level of
recursion.

We have log(n) number of levels and for each level, we're doing O(n) time complexity, so the overall time complexity
is: `O(n log(n))`.

**Note: At each level, we have n nodes. So total number of nodes which is the time complexity is number of nodes at
each level multiplied by number of levels: T: O(n * log(n)). In other words: n + n + ... + n (log(n) times).**

`Memory: O(n)` because at any point we have to create two temporary arrays to build the original array.

Is merge sort a stable sorting algo?

**We can code it in such a way that it does.** It depends on how we handle the equality case in the merge() step. If an
element in left subarray is
smaller, if we put it in the merged array before the right equal element in the right subarray, this makes sure that
this is stable.

**Merge sort in most cases is preferred over insertion sort.**

**Is log n really that much more efficient than n?**

**Yes the comparison between n and 2^n is the same comparison between n and log n . log n grows so much more slowly than
n**.

Think about decrementing 8 to 1:

- in O(n), it's 8 -> 7 -> 6 -> ... -> 1
- in O(log n), it's 8 -> 4 -> 2 -> 1

So for really big numbers, it's gonna be a lot faster. **So O(log n) is very very efficient compared to O(n)**.

## 13 QUICK SORT

Very similar to merge sort.

The idea is instead of splitting the array into two equal halfs and then sorting those halfs, we're gonna pick a random
value and for convenience
we usually pick the rightmost(last) value and this is called the pivot value.

We're gonna iterate through every single value in the input array except the pivot, so every value before pivot and
we're gonna compare
that value to the pivot and every value that's less than or equal to the pivot, is going to be in the left partition of
the array.

So in the left partition, every value is less than or equal to pivot and every value that's greater than the pivot is in
the right partition.

We can perform the partition in-place which means we don't need to allocate any extra memory to do the partition.
For this, we need two pointers. One pointer is for iterating the array and the second pointer is gonna tell us where we
should insert the next value that is less than or equal to the pivot.

When we hit a value that is less than or equal to the pivot, we swap the values that the pointers point to and move the
second pointer forward.

The first pointer(for loop) moves forward until it reaches the pivot.

We wanted to partition the input array such that every value less than or equal to the pivot is moved to the left side
and every value greater than
pivot on the right side of those smaller values(but the pivot is at the end).

Where should we put the pivot itself to satisfy that?

We can use where our second pointer points at currently. Every value before the pointer is less than or equal to pivot.
That is a good position
to put our pivot at.

So now we perform one last swap between where our left pointer(the pointer that marks the end of our small values) and
our pivot.
Why? Because now every value before the l pointer is less than or equal to the pivot, so l is a good spot for pivot(note
that pivot should be
before all the elements of the right half, so l pointer is the ideal place for it).

Just because we partition the array, does not mean the sub-arrays are sorted in themselves. But what is true is that
every value on the left subarray
is less than every value on the right subarray.

Now split the array into two pieces based on where the second pointer is(the pointer that points to the last small
element which is now where
the pivot which was swapped, lives).

Now the recursive step comes in. Now let's run quick sort on left and right subarrays.

The last element of left subarray is already in sorted order because it was the pivot. Everything to the left of it is
less than or equal to it and
everything to the right of it is greater than to it. So we can ignore this element. So it does exist but we're not
focusing on it, when we run
quick sort on left subarray, we ignore the last element, because the last one is already where it needs to be. This is
always gonna be true for the
pivot value.

Now the one to last element of the left subarray is the pivot(we ignored the last element because it's already sorted),
now repeat the quick sort.

**With quicksort, we're not allocating any extra memory.**

The time complexity **looks** similar to mergesort because we're breaking it up roughly into equal halfs, but the thing
about the pivot is
we're always picking the last element and **it might not result in equal halfs**. For a not equal partitions, consider
this example:
[1, 2, 3, 4, 6], after partitioning(which happens in place, no extra memory, we just use pointers), we
have: [1, 2, 3, 4] and [6] and ... .
The visualization is:

The height of the tree is `n(the case where we don't have equal halfs)`. But if we split it into equal halfs, we know
the height of it is gonna be `log n`. But when we're not splitting into halfs, the height of the tree in the worst case
is gonna be `n`.

Now for each level, we have to iterate through approximately the size of the input because that's approximately how many
elements we have on each
level. Why approximately? Because we don't iterate on the pivots.

**In that case, the overall time complexity becomes `O(n^2)` in the worst case. This shows quicksort is not necessarily
better than mergesort. But on
average, this is not gonna happen. This was the worst possible case where the input is already sorted.** One way to get
around this, is not to pick
the pivot as the last element, it's to take the first value, the middle value and the last value and among those three,
choose the middle value and then use that as the pivot.

So the way we've been selecting our pivot is a bit naive. There are optimizations that we can do which will help us to
make sure that we don't hit the worst possible case.

So on average(if we do split the array into two roughly equal halfs), then the time would be similar to merge sort. The
**height will be log n** and
since each step(level) is gonna be am O(n) operation, then the overall time complexity for quick sort on average
is: `O(n log n)` but the worst case
is `O(n^2)`.

Q: Is quicksort stable?

A: generally speaking no. There is a way to technically modify it so that it is stable.

Why it's not stable? Let's say: [7(A), 3, 7(B), 4, 5]. We pick 5 as the pivot. After the first iteration, we would have:
[3, 4, 7(B), 7(A)], the original relative order of equal elements are not preserved. So this algo is not stable.

![](../img/5-sorting/13-1.png)

Time:

- worst case(if input is already sorted): O(n^2)
- average case: O(n * log n)

- Space: O(1)

Usually we care about big O or worst case which is O(n ^2) but generally speaking, people consider quicksort to be an
efficient
algo, O(n log n) on average.

## 14 BUCKET SORT

It can run in O(n) even in the worst case(note that O() is only used with worst case but we unofficially use it for
average case and ... in this course). So it's super efficient. So why did we even bother learning the other algos that
are slower by having for example O(n logn)?

Because it's very rare that we're able to use bucket sort. It's sorta a forbidden technique which rarely gets to be used
and that's because there needs to be certain constraints for the problem(input). We're only allowed to use bucket sort
if we're guaranteed that all the values that we're sorting, fit within a finite range.

Now typically when you have an array of integers, usually the integer is bounded by a 32-bit integer or 64-bit integer
and therefore we would have a range like -2^32 all way to 2^32 . So we could say that that's our range but that's a
really big range and that doesn't usually qualify for bucket sort. We're talking about smaller ranges like 0 - 100 or
0 - 100,000 .

Now for every single value in our range(duplicate values not included), we're gonna create a bucket. Each of the buckets
is gonna be a value.
For example: input is: [2, 1, 2, 0, 0, 2]. Now we count how many of each element we have and the buckets would
be: [2, 1, 3] which
the first element maps to the number of zeros, second maps to number of ones and third maps to number of twos.
or if the values were [1, 0, 4, 1], the buckets would be: [2, 1, 1].

Q: What is the time complexity of counting these?

A: O(n) .

Every sorting algo we saw, would swap values. But bucket sort does not do that at all. By the time we have counted all
the values, we don't even
need the input values at all, we don't care what these values are anymore. We're just gonna start overwriting them with
two nested loops.

The outer loop goes through the counts array. The inner loop's variable is not used! We just want to iterate that many
times. In the inner loop,
we iterate x times and x is the value of the current element. Then overwrite the input array.

### Time and space

Q: Why is this algo O(n)? Don't we have nested loops?

A: How many times does that nested loop portion actually gonna run. Remember **just because we have two nested loops
doesn't mean the time complexity is O(n^2).**
The **total** number of iterations for the nested loop is `n`(number of elements in the input array).

Space:

The size of the array we create is whatever the range of values of the input arr is. As long as the range is not very
large, we assume the range
is a constant so the memory we're allocating, is O(constant) where constant is the range and we know constant is reduced
to O(1).

- Time: O(n)
- Space: O(1)

Q: Is bucket sort a stable algo

A: No. Because when we overwrite the array, we're not even caring about which 2 came first. We're not even swapping the
values, we're just overwriting,
so it's definitely not stable. So it doesn't preserve the relative order of the equal elements at all.
But if we wanted to, technically we could make bucket sort a stable algo. Because as we count the elements, we could
preserve the order somehow.
If we make the `counts` var a linked list where the order of equal elements is preserved.

But it's pretty rare that bucket sort is used on anything other than an array.

Most likely you won't be able to run bucket sort on the input that you're given. But if you ever are given an input
where bucket sort can be run(values
are within some specified range), don't ever use any other sorting algos because they're not gonna be as efficient as
bucket sort.
Otherwise, most likely you will end up using either merge sort or quick sort and merge sort is generally more common.

![](../img/5-sorting/14-1.png)