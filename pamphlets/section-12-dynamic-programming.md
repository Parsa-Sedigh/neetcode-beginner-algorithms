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
In count number of paths slide: since we can only move down or right, every path is gonna be exact same length. Because as we move down,
we're getting closer to the bottom right, as we move to right, we're getting closer to bottom right.

Caching in 34-1: As we move towards the goal, when we get to it, we find out in how many ways from which cells, we can reach the goal.
This number of paths are revealed first for the closes cells to the target, because we're returning 1 to the caller.
![](../img/12-dynamic-programming/34-1.png)
So first we get the result for cell[3][2] and then for the earlier cells ... .

For every position, to get how many ways we can reach the target cell from this cell, we can take the value below and value right and add
those sub-problems together. We have some repeated work.

In the slide, you can think of grid as the cache because it's our cache in this case is a 2-d arr.

The cells(cache cells) at the row 3, all get value 1 because from those cells we can only reach the target by going to the right,
hence only 1 path from each to the target.
Also the cells at the last col are 1 as well.

So cells at last row and last col are can go to the target with 1 path.

The numbers on cells are the number of paths we can reach target from that cell. That grid represents the cache.
![](../img/12-dynamic-programming/34-2.png)

---

### Bottom-up approach:
Why should we even start at the top and work our way down and then recursively solve the sub problems and go back up. Why not just
immediately start at the bottom and then fill in the values and then get to the top and ultimately have the overall result which is number of 
paths from top left.

But the benefit of bottom-up is sometimes we don't have to declare all that extra space.
We don't need a 2-d grid for storing the result anymore, we only need to store the results of prev row, in contrast to
top-down approach which requires more space(O(n * m)).

The bottom-up approach usually has a lot less code than the recursive approach, but it's usually difficult to come up with unless you have
a good understanding of the recursive approach.

Start at the bottom(bottom right). At each iteration, we go through a row from right to left and at the bottom and
work upwards.

At the last row(first iteration): We're assuming from the target to the target itself, there's 1 path. Yeah it makes sense that
it's 0 paths, but as the base case we put 1 there, because that's what allows our math to work. Because if we put 0 there, according
to the code, all the values gonna be 0 in whole grid, but that's not correct. So we put 1 in the target cell itself.

When we computed the bottom row(in slides, row #3), we go the prev row. Now we know the prev row results. For each position to calculate,
we add the cell below and next cell(note that we go backwards meaning from right to left).

So we're going in the same order that our recursive algo(top down(memoization) dp) did.
![](../img/12-dynamic-programming/34-3.png)