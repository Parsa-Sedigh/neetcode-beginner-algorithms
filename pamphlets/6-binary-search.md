# Section 06 BINARY SEARCH

## 15 SEARCH ARRAY

**To use binary search, arr should be sorted.**

Very related to sorting. Because binary search can only run on an input that is already in some type of **sorted order
**.

Every time, we're gonna eliminate half of the possibilities.

If the input is not sorted, we can't run binary search. So if it's not sorted, best we can do is go through every
element to find the
element we want which will be `O(n)`.

In binary search, with every iteration of loop(while), we're eliminating at least half of the elements. So the length
would be get divided by
2 in every iteration: n/2*2*2 ... . We continue dividing it by 2, until it equals to 1. We talked about this in merge
sort:

How many times can we divide a value by 2 until it's equal to 1? This is gonna tell us how many times the loop in binary
search is gonna execute.

The number of times is: log base 2 of n. Usually we don't mention base 2. So it's gonna be `log n` which is the time
complexity of
binary search. That's how many times the while loop is gonna execute.

O(log n) is much more efficient than O(n).

- Time: O(n)
- Memory: O(1)

## 16 SEARCH RANGE

Variation of binary search algo.

We're given a range of values instead of a sorted array. So we're given a lower bound and an upper bound(low and high
parameters), we're not
given a arr(or a sorted arr).

We're trying to guess the number that satisfies a condition in the given range.

`T: O(log(n))`. In search arr type of binary search, n is the length of the arr. But in this case, n is the length of
the range that we're given. 