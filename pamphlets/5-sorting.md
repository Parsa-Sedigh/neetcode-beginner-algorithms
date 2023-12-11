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

## 13 QUICK SORT
Very similar to merge sort.

## 14 BUCKET SORT