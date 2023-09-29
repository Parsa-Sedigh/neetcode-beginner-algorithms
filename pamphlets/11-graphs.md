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
![](../img/11-graphs/29-4.png)

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

## 30 Matrix DFS

## 31 Matrix BFS

## 32 Adjacency List