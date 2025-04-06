# GraphNode used for adjacency list
class GraphNode:
    def __int__(self, val):
        self.val = val

        # the neighbors are gonna be pointers(edges), they could be directed or undirected.
        self.neighbors = []

# Or use a hashmap
adjList = {"A": [], "B": []}

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

###################

# Build an adjacency list out of the directed edges:
adjList = {}

# Go through every single edge(which is a pair of nodes)
for src, dst in edges:
    if src not in adjList:
        adjList[src] = []

    # Why we add the dst to the hashmap as a key? Because we wanna at the very least make sure that every node that we saw in the
    # list of edges, is added to the adjacency list, even if it doesn't have any neighbors. Because we want to at least have an empty
    # list for that node to confirm it doesn't have any neighbors.
    if dst not in adjList:
        adjList[dst] = []

    # assuming that the graph is DIRECTED, just add dst to the neighbors list of src.
    # Note: If graph is undirected, we should add src to the neighbors list of dst as well.
    # So we would also do: adjList[dst].append(src)
    adjList[src].append(dst)