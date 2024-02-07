## 09 FACTORIAL
### One-branch recursion
n! = n * (n - 1) * (n - 2) * ... * 1

5! = 4 * 4! ...

n! = n * (n - 1)!

Recursion is all about sub problems.

The best way to represent recursion -> decision tree. If we only have 1 decision at a time -> one-branch recursion.
As we go down the tree, we say before computing the parent, we have to compute the children(sub-problems). When we hit the base case,
we go back up to the original function call.

To compute n!, we have n steps:
- time: O(n)
- space: O(n)

The time complexity is the same as we used a while or a for loop where we start at n and we decrement it by 1 each time to do the computation.
So there's no benefit in this case of using recursion. But the space complexity of recursion is worse than doing this with while loop,
because with recursion, we get O(n) memory complexity, but in while loop, we don't allocate memory(O(1)).

The recursive solution for this problem is less efficient than the iterative one.
![](../img/4-recursion/9-1.png)

## 10 FIBONACCI
### Two branch recursion
The recursive solution for this problem is less efficient than the iterative one.

At each step, first we go to the left subtree and then right subtree.

Iterative:
- time: O(n)
- space: O(1)

recursive:
- time: O(2^n)
- space: O(n) - maximum number of calls in call stack

**Note: For Fibonacci recursive implementation or any recursive algorithm, the space required is proportional to the maximum depth of 
the recursion tree, because, that is the maximum number of elements that can be present in the implicit function call stack.**

To analyze the time complexity of recursive, looking at the code is not gonna help us.

The fact that we have to break it up into two sub-problems at each step, comes from the fact that we have two branches in our recursive tree.

Now in this recursive tree in the img, how many times are we gonna have to break it up into two sub-problems?
**In other words, what is the height of this decision tree?**
**The height of tree is basically how many levels does this tree have.**

Now the longest path(worst case) to the leaf(why leaf? To find the level), is `n` where that path is the nth fibonacci that we're trying to compute.
This means the number of levels is `n` as well, which means the **height** is `n.`

Now to find the time complexity, we need to find out how many function calls(nodes) are in this decision tree?

At each level, roughly, the number of values doubles(we would have n times `* 2`). So time would be: O(2^n).
Why n times? Because it's the height.

In general, to get the number of fibonacci values(nodes) in the last level(leaf) theoretically with math, it would be is calculated by noticing:
The number of nodes at each level is doubled. So in the nth level, it would be: 2 * 2 * ... * 2 = **2^n which is the number of nodes in the last level**.
Note: This is a rough estimation. n is roughly the height of the tree and we assumed that each level is full. So in realty, the 2^n is 
an **upper bound** for the number of values we can have at the last level.

1, 2, 4, 8, ... is a series where next one is the double of previous. This is special in math, it's called power series, the last val always
dominates all the previous values. Here, 8 is grater than or equal to all the previous ones combined.

In our case, 2^n is an upper bound for the last level, it's also an upper bound for the total number of values in this decision tree.

So 2^n is how we can bound this in terms of big O time complexity, even though 2^n is not the precise number of values in the decision tree,
but it's still a very good upper bound because we don't care about constants when calculating time complexity.
![](../img/4-recursion/10-1.png)