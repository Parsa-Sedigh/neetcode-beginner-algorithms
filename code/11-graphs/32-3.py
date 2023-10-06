# Shortest path from node to target
from collections import deque


def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)

    queue = deque()
    queue.append(node)

    while queue:
        # Take a snapshot of the length of the queue
        for i in range(len(queue)):
            curr = queue.popleft()

            if curr == target: return length

            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)

        # When we visited each level, we increment the length. This shows the length pf the path to each level that we go and at the
        # end, it's gonna represent the length of the path to the target.
        length += 1

    return length

# We've probably built the adjList ourselves!
print(bfs("A", "E", adjList))