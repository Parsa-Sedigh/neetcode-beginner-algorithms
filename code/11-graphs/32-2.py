# count paths(backtracking)

# T: O(N^v) - N is average number of edges that each node has and v is number of vertices. Now the longest path we can go(worst case)
# is v. So the height of the decision tree is v. Now on average for each vertex we can have N edges. So N decisions on each node of
# the decision tree. So at each level of decision tree, the number of nodes is multiplied by N. So time complexity is:
# O(N^v).

# Note: In worst case, each vertex has v-1 edges. So time complexity can be O(v^v).

# M: O(v). The maximum height of decision tree could be v. Meaning to go from `node` to `target`, we have to visit all vertices.
def dfs(node, target, adjList, visit) -> int:
    # Has this node already been visited? If it has, there's zero paths from here to the target.
    if node in visit: return 0
    if node == target: return 1

    count = 0
    visit.add(node)

    # We have the neighbors in our adjacency list. We don't have to go manually in 4 different directions.
    for neighbor in adjList[node]:
        # Call dfs on each of the neighbors.
        count += dfs(neighbor, target, adjList, visit)

    # backtrack part
    visit.remove(node)

    return count

print(dfs("A", "E", adjList, set())