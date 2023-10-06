# count paths(backtracking)
def dfs(node, target, adjList, visit):
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

