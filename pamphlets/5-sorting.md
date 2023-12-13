## 11 INSERTION SORT
Sorting are usually applied to arrays but you can apply it to other DSs including linked lists and ... .

We consider any array of one element, sorted. So first element is sorted, the next sub-problem is to sort the first two values.
Then first three values and ... .

Since we're doing it with sub-problems, we could solve this using recursion, but it's not useful in this case. We're gonna solve it with
iterative approach.

We start at the second element, because we know the first element is already sorted. Our goal is to figure out where to put the current element
that we're at? **(previous values are already sorted)** 

**Note: If the current element is greater than the previous one, we don't need to compare it to the smaller values in the already sorted subarray.**
Because the subarray is already sorted. So if current is greater than prev, OFC it's gonna be greater than any value to the left of the prev. Because
every value to the left of prev is less than or equal to prev(they are already sorted).

It's called insertion sort because we're taking one value(curr) and inserting it into a sorted array(prev values).

`j + 1` is current element and `j` is previous element(which is in the sorted subarray).

As long as we have a way to compare two values like characters(like sorting based on alphabetical order), we can sort them. Maybe sorting words as well,
based on their first character.

### Stable vs unstable
The difference of a stable and unstable sorting algo, is let's say we have 7, 3, 7 as input. The sorted result is: 3, 7, 7.
The stable sorting algo would put the first 7 to also appear before the second 7 again in the result.
It preserves the original relative order of the elements that are equal.

In other words, **the stable sorting algo will preserve the original order when there's a tie.**

**Unstable sorting might preserve the original order of equal elements, but there's no guarantee.**

Insertion sort is stable. 

**It's preferred to keep an algo stable, if you can.**

### Time and space
When we have an array as the input that's already sorted, when we run insertion sort, the inner while loop won't execute at all and we only
iterate through the array. So time is `O(n)`.

So just having a loop in an algo doesnt mean it's necessarily gonna execute in all times.

So **the best case time complexity(which would occur if the input is already sorted in this algo) is: n**. We don't use O() here because
it's not used with the best case, it's for worst case.

Worst case: Occurs when input is in reverse order(based on what order we wanna sort). In the worst case, for every single value that we
iterate, the inner while loop would have to execute the maximum number of times until that value shifted all the way to the left.
But it's **not** O(n^2). Because for input of size 4, it's not n^2 because the while loop doesn't loop 4 times for each element.
It loops: 1 time(for the second element, we're skipping the first el), 2 times for the third element and 3 times for the forth element. 
So it doen't loop 4 times per element. So we have: 2 + 3 loops for the while loop instead of 4^2 which is 4 + 4 + 4 + 4.

But remember we just want an approximation and that's enough for us when we're doing big O time complexity.

Note: When you have two nested loops it's usually correct.

Note: 1 + 2 + 3 + 4 is bounded by 4 + 4 + 4 + 4(n^2). For proof, look at the vid. Basically it's half the size of n^2(4 + 4 + 4 + 4), so we can consider
it as n^2 because 1/2 * n^2(n is input), is considered O(n^2).

- stable
- `worst: O(n^2)`
- `best: O(n)`

## 12 MERGE SORT
It's common because it's efficient, since we're splitting it into halfs and it does make things more efficient.

The main idea is to take the input arr and split it into two approximately equal halves and then for those halfs, split them into two approximately
equal halfs and ... continue to split each sub array until we can't split them anymore, which would mean we have individual elements left to sort.

We break the original problem into sub-problems.

This algo is a 2-branch recursion because we're splitting the arrays into halfs.

**Divide and conquer: take the original problem and divide it into sub-problems and then solving those sub-problems before solving the original problem.**

When merging two sorted arrays into a third array, we need 3 pointers:
- a pointer for the first arr
- a pointer for the second arr
- a pointer for the result array

![](../img/5-sorting/12-1.png)

When we merge() the left and right halfs, we do need to create extra memory.

### Time and space
Starting with an array of length n, how many times can we split it by half? In other words, how many levels are there to this recursion?

It's the same number of times where we can take `n` and divide it by 2. Note that when n = 1, we hit our base case. So what's the math
formula for how many times we can take `n` and divide it by 2 until it's equal to 1? Well if we were starting at n=1 and then multiplying
it by 2 every single time, that would be `O(2^n)`, but we're doing the reverse of that. We're dividing it by n. So what we're asking is we have
n and we wanna divide it by 2 and then divide it by 2 and ... , so sth like: n / (2 * 2 * 2 ...) , so it's:

`n / 2^x` where x is the number of times we're gonna divide n by 2. Now we know we wanna keep dividing it by 2 until we hit the base case:
`n/2^x = 1`, now by doing some algebra, we have: `n = 2^x`. We care about x, that's how many levels are going to be in this merge sort algo.
We can take the log of both sides of the equation. We use log base 2 of n and by doing some math, `x = log base 2 of n`.

So how many times we can divide n by 2 until n = 1?

The log base 2 of n is how many times we can divide it by 2 until it's equal to 1.

Watch the video from 13:30 to 16:00 to learn the math behind log base 2 of n.

In logarithm, if the base is 2, it's omitted. Log base 2 of n is the number of steps that we're going to have to divide n by 2 until it's 1.
But what's the time complexity of **each step** of this algo? It's O(n). It has to do with the merge() step. We're gonna do O(n) in every level of
recursion.

We have log(n) number of levels and for each level, we're doing O(n) time complexity, so the overall time complexity is: `O(n log(n))`.

`Memory: O(n)` because at any point we have to create two temporary arrays to build the original array.

Is merge sort a stable sorting algo?

**We can code it in such a way that it does.** It depends on how we handle the equality case in the merge() step. If an element in left subarray is
smaller, if we put it in the merged array before the right equal element in the right subarray, this makes sure that this is stable.

**Merge sort in most cases is preferred over insertion sort.**

Is log n really that much more efficient than n?

Yes the comparison between n and 2^n is the same comparison between n and log n . **log n grows so much more slowly than n**.

Think about decreenting 8 to 1:
- in O(n), it's 8 -> 7 -> 6 -> ... -> 1
- in O(log n), it's 8 -> 4 -> 2 -> 1

So for really big numbers, it's gonna be a lot faster. **So O(log n) is very very efficient compared to O(n)**.

## 13 QUICK SORT
Very similar to merge sort.

## 14 BUCKET SORT