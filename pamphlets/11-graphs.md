## 29 Intro to graphs
Common ways of representing graphs:
1. matrix
2. adjacency matrix(much less common)
3. adjacency list

Linked lists are a form of graphs. They're a subset of graphs and another subset of graphs are trees whether it's binary trees or other
kinds of trees.

A graph is made up of nodes and possibly some pointers connecting the nodes together.

Nodes = vertices

pointers = edges

When we talked about binary trees and BSTs, we mentioned that they never have cycles.

`E <= V^2`. V is number of vertices(nodes). Why?

Because what we're saying is from every single node aka vertex, we could have a pointer going to every other vertex.

Note: We can have an edge going in on itself. So a node can be pointing to itself.

Note: For every single node, we could have `V` edges. Where v is total number of nodes.

Note: Technically we can have duplicate edges(like multiple edge from A to B), but usually we don't consider that where it comes to graphs.
![](../img/11-graphs/29-1.png)

Note: As you see in the img, we have a pointer(edge) from A going to B and we also have a pointer from B going to A. That means
we can go between A and B back and forth. We say there's a **cycle** formed between A and B. There are other cycles in the img

When every single pointer(edge) has a direction, this is referred to as a directed graph. Trees and linked lists are directed graphs.

Undirected graph: For drawing them, we can use `<--->` or `---`, these two indicate that that edge is undirected, meaning you can go
in either directions, you can go from node1 to node2 or node2 to node1.

It's most common to represent a graph, using adjacency list.

---
### Matrix
A matrix is a 2-dimensional array. It can be used to represent a graph which is what we're gonna do in this case.

Use r(row) and c(column) instead of x and y to show coordinates. `r` and `c` are used in matrix but in adjacency matrix,
an index represents a vertex itself.

In the img, you're allowed to move in 4 directions(top, right, bottom, left). You might be able to move diagonally, but it's typically
less common.

How does the matrix in the img represent a graph?

You could say that free spaces(zeroes) are nodes and the 1s are gonna blocked out. Now where are the edges? I said we can move left,
right, up and down, so the edges are the green lines. The edges are undirected.

Note: These edges exist because of the rules that we defined. I said we can move right, left, top and bottom. Maybe we could've defined
we could move diagonally and other kinds of moves.

This was a common way of representing graphs in interviews.
![](../img/11-graphs/29-2.png)

For now we're just going over how this is represented(representing a graph), later on we'll talk about how common algos can be implemented
using this. There can be a lot of edge cases.

### adjacency matrix
We'll talk about this is less common than the other two.

In this case, the zeroes are not nodes anymore.

In adjacency matrix, the dimensions represent the nodes. Typically it's a square matrix. Let's say the size of matrix is v * v where
v represents the number of vertices. That's OFC why it has to be a square, both the number of rows and cols are v, hence becoming a square.

In adjacency matrix, when there is an edge, it's a directed edge, so in adjMatrix[v1][v2] = 1, it means there's a directed edge from v1 to v2.
Now if we wanna know if there is an edge from v2 to v1? We look at the adjMatrix[v2][v1]. The order of indexes represent the direction of the
edge.
![](../img/11-graphs/29-3.png)

Note: What's the maximum number of edges we could have with an adjacency matrix?

Maximum E = V^2

Q: Why is it rare to use an adjacency matrix?

A: No matter how many edges we actually have, to represent a graph we're using an entire matrix. That means the space complexity is `O(v^2)`
where v is number of nodes. We could represent the exact same info of graph, in `O(V + E)` which in the example of img, since V = E, it
would be reduced to O(V + V) => O(V). So why would we use a matrix which takes up extra space and doesn't provide additional info?
That's why it leads us to next way of representing a graph, adjacency list.

### adjacency list
The most common way of representing graphs, especially in interviews(matrix is also common).

It's similar to linked lists and trees.

Note: The value of a GraphNode could be anything(object, integer, ...).

In linked lists, we could either had a next pointer or prev pointer. It BSTs, we could have a left or right pointer. But with generic graphs,
we could have any number of pointers. We represent them with `neighbours` field of a GraphNode. In the context of social network,
we could name this field `following`. Instead of predefining the number of pointers we can have for a GraphNode, we use a list.
What is the type of elements in neighbours list? It's gonna be an array of `GraphNode`s.
For example for node 1, it's neighbours are the node 0 and node 1 itself. And the neighbours of node 3, is node 1.

The neighbours list refers to which nodes is this node pointing **at**?

This is a bit more space efficient than the adjacency matrix. Because we only contain pointers for nodes that actually exist. We only
have space for edges that actually exist.

If we had undirected edges, both nodes would have the other node in it's neighbours list.

When we have undirected edges, we're assuming that there is a pointer going both ways.

Now let's look at common algos when it comes to matrices(for representing a graph) and then later we'll talk about adjacency list.

![](../img/11-graphs/29-4.png)

## 30 Matrix DFS
If the constraint of "can't visit same cell more than once" didn't exist, the answer of question would be `infinite`. Because we could move
between 0s infinite times.

This question might remind you of backtracking and that's because it pretty much is. There is a big overlap between DFS and backtracking.

The DFS in matrices is more complicated than in binary trees.

Look at `30-1.py`:

We start at top left. The `grid` param is the matrix itself. Now what are our choices? We can move in all four directions.
We can potentially move out of bounds of the grid(matrix). That's what the first base case is going to be(to check it).

Note: `len(grid)` gives us the number of rows, length of one of the rows for example the first row(because every row is gonna have
the same length, because the grid is a rectangle), which would be: `len(grids[0])`, gives us the number of columns.

In the code, we're calculating ROWS and COLS everytime we call the function(we would have recursive calls), that's unnecessary to do,
we could pass in ROWS and COLS as params of function. But it doesn't change the time complexity, so this isn't such a big deal.

`min(r, c) < 0`:

In the base case 1, one case is that our row(r) or column goes out of bounds, become too small. So we could check: `r < 0 or c < 0`.
Or you could simplify that into: `min(r, c) < 0`. Because we just care about one of the r or c become too small.
Now if we end up out of bounds, that means we did not find a path to the destination in this current path that we went.
So we would `return 0`. Why 0? Because this DFS is supposed to count the number of paths. There are also a few more conditions where we 
would return 0.

`r == ROWS or c == COLS`:

Another condition in base case 1, is our `r` and `c` instead of being too small(previous condition), they could be too big. Our r could be
equal to the number of rows. Now why we're checking if it's equal to the number of rows instead of greater?
If r ever goes out of bounds, if it equals ROWS, then we also return 0(similar for `c`). We did not find the right path, we went out of bounds.
Why can't we take the max(r, c) and check if it's greater? Because remember the number of rows and columns(ROWS, COLS variables) might not
necessarily be equal.

Note: Yes we used min() for checking if we went out of bounds in top or left corners, because the 0 is always the starting point but the
ending point could be different(rows could be more than columns or vice versa, so the ending point is not fixed).

`grid[r][c] == 1`:

If we reached a blocked position. We're not supposed to be in that position. So we stop searching by returning 0. We're not gonna continue 
our recursive case, because we're not allowed to even visit this position, so we're gonna stop immediately and return 0. Basically
we're saying by visiting the current position, there are no valid paths that reach the destination.

`(r, c) in visit`:

If we reach a position that we've already visited before.

Second base case:

We reached the destination. How do we know we reached the destination? Well, it's at the last row, last column, so 
`if r == ROWS - 1 and c = COLS - 1`, then we return 1, that means we found a single path.

The hashset is gonna be reused throughout the recursive function. It means we're not creating a new hashset everytime we make a recursive call,
we're passing in the reference to that exact same object. Every recursive call is gonna have access to that exact same object.

Note: Let's assume there's always going to be at least one valid path in this matrix. But if you're not sure, it's worth asking that
as a clarifying question.

The reason we're using a hashset, is because it's easier to code, to just add a pair of values. We know adding and removing from a hashset
is `O(1)`. But alternatively, you could use a two-dimensional array with the same size of the matrix(`grid`) as well for `visit` as well.
Because basically what we're gonna do with `visit`, is to mark the positions that we've already visited.

Note: If you're allowed to modify the `grid`, you could also as you visit the position, mark it as a 1 to indicate that it's already been
visited. But it's not always safe to assume you can modify the input `grid`, so we ignore this for now.

Q: How the `count`s are gonna get returned?

A: When we move to a new position, we're gonna have a new count variable initialized to 0. In the new position, we're counting how many ways
from this new position, can we reach the destination and when we find that result, we're gonna return that to the previous position that we were
at and this returning gonna repeat until we hit the starting position of the grid((0, 0)).

Now since we have DFS, we're not gonna go along the multiple paths(if we could) simultaneously, we're only gonna do one at a time, we're gonna go
as deep as we can in **one** of them and then we're gonna backtrack and then we're gonna go along the other path.
Looking at the code, we move down as deep as we can and then we go to other directions.
So when we have multiple choices in a position like going right or going down, first we go down as deep as we can.

Look at the img, at position (3, 2), we can reach the destination. Now we know (3, 2) is marked as visited(it's in visited hashset).
Now before returning 1 to the previous node(which will again return 1 to it's previous node, all the way to the first node).
But before returning count(1), we remove (3, 2) from the hashset, because we wanna backtrack. Why (3, 2) and not (3, 3)?
Because at (3, 3) we hit the second base case and we return 1 to the (3, 2).  So now we're at r=3, c=2 and we would hit the line where
we have: `visit.remove((r, c))`, so we mark it as not visited and we would mark all the nodes in the path that led to the valid destination,
until we hit a node that had multiple choices to go. Why? Because we always choose to go down and deep as possible, so we didn't go
to other directions for some of the nodes that we could. So we backtrack until those nodes and then we go to other directions of those nodes.
Now note that the nodes that actually led to the valid destination and were a head of the node that we've backtracked to, are now marked
as unvisited. So now that we're examining the other directions of the node, we can actually visit those nodes that led to the valid
destination again. Now why is this allowed? Look at the img, in position (0, 2), we could reach the destination using 2 paths(blue and purple).
That's why when we reach the destination and then backtrack, we also mark the nodes as unvisited until we backtrack to a node that had
multiple choices and still have some paths to explore.
![](../img/11-graphs/30-1.png)

Those blue and purple paths are two different paths, so they are allowed to visit the same node like (1, 2), (2, 2) and ... and even
the detestation position itself.

The questions says only a **single** path can't visit the same position twice, but multiple paths can visit the same position, in fact they
have to, if they wanna both reach the destination position. The destination position itself is actually among the nodes that multiple
paths actually have to visit, in order to get there.

Note: From (0, 2) we can reach the final destination in 2 ways and since we return the count(2) to it's previous nodes((0, 1) and (0, 0)),
therefore from (0, 1) and (0, 0) we can also reach the destination in 2 ways. So now we can reach the destination from the starting
position in 2 ways which is actually our final result of the problem overall(the final value that we return from all of the recursive calls).

### Time and space complexity
Calculating these in this case is complicated, so we can think about it in simple way but it's not super precise.

Let's suppose the worst case is where the grid is all zeroes. We don't have any blocked positions. In that case, the length of a valid
path could be the size of the matrix. So thinking about it in terms of a decision tree: from any position, we have 4(we can go
left, right, up or down) choices. Now OFC we know some of those choices are gonna execute the first base case where we either go out of bounds
or maybe we visit the same position twice or we visit a blocked position, but like I said, this is an imprecise way but it still gives
us an idea of the upper bound.

Note: A path in the decision tree represents a valid path in the matrix.

So for every node we have 4 choices and the **height** of the decision tree is gonna be the size of the matrix which is 
`<number of rows> * <number of columns>`. Now recall from binary tree analysis, the time complexity is gonna be: 
`<number of branches>^<height of the tree>`, so: 4^(R * C). Or if we say: number of rows = N, number of cols = M, it's gonna be:
4^(N * M).

The <number of branches> in this case is 4.

`So the time complexity: O(4 ^ (N * M))`. So DFS is not efficient, but that's expected when it comes to brute force DFS(backtracking).

Memory complexity: Would be the recursive call stack. The thing that matters for the space complexity of recursive calls is the number
of outstanding function calls at the same time(need to be processed).

In this case, the size of the call stack at the same time in worst case is the size of the matrix. So:

`Memory complexity: O(N * M)`.

We could also say that O(N * M) is also the memory complexity from our `visit` hashset, because that is also going to be the size
of the grid, or instead of having a hashset, you could create a two-dimensional array with the same size of the input `grid`, to keep
track of the visited positions.

Note: DFS on a matrix comes up quite often.

![](../img/11-graphs/30-2.png)

## 31 Matrix BFS

## 32 Adjacency List