# Section 12 DYNAMIC PROGRAMMING

## 33 1-Dimension DP
Fibonacci sequence is 1-dimensional DP.

For calculating, f(5), we calculate f(2) until f(5). We can solve fibonacci using a loop. So it would be O(n).

We can convert the recursive solution of fibonacci and convert it into a DP problem.

The recursive solution is O(2^n). Because we have 2 branches at each step and the max height is n(some levels are not filled when
looking at decision tree).

We're doing a lot of repeated work. Look at the two subtrees with the root of 3 and three subtrees with the root of 2. They're the same.
To eliminate this repeated work, we can use memoization.
![](../img/12-dynamic-programming/33-1.png)

If we see we're creating the same decision trees to solve the same sub-problem, like calculating the second fibo(f(2)).
So after we solve calculated a sub-problem once, we can cache the result and the params that caused that result.

In the img, the cache is drawn as arr, but consider it a hashmap.

Note: The numbers in decision tree, are the `n`s not the results.

The decision tree with memoization is the green one:
![](../img/12-dynamic-programming/33-2.png)

You can see that we essentially get a linear tree. Yeah you can see each node has a right child as well, so the size is not just n it's
2 * n, but in big O, it would still be O(n).

So the time complexity reduced from O(2 ^ n) to O(n) when we implement memoization which is also called top down DP.

Memoization is top-down DP.

Types of DP:
- top-down(memoization)
- bottom-up: more difficult because we can't just take the recursive solution and add caching to it(what we do for top-down).

Note that the repeated work is eliminated in both forms.

Bottom-up for fibo is in 33-3.py

The approach where we don't use recursion at all like in 33-3.py, it's called true dynamic programming. Some people don't consider
memoization a DP at all and they only consider approaches like 33-3 to be DP.

We wanna calculate f(5). Why start at f(5) (top) and then go top-down, when we can go bottom-up. Start at the base case immediately and then
work our way upwards. Because we know the value of base case(because it's the base case!).

The most efficient way of solving fibo is bottom-up DP which is in 33-3.

DP takes a big problem like f(5), but to do that we have to solve sub-problems like calculating f(4) and f(3) and ... .

## 34 2-Dimension DP