
from collections import deque


def topological_sort(vertices, edges):
    graph = {i: 0 for i in range(vertices)}
    neighbour = {i: [] for i in range(vertices)}
    for edge in edges:
        parent, child = edge
        graph[child]+=1
        neighbour[parent].append(child)

    queue = deque()
    for elem in graph:
        if graph[elem] == 0:
            queue.append(elem)

    res=[]
    while queue:
        current_node = queue.popleft()
        res.append(current_node)
        for child in neighbour[current_node]:
            graph[child]-=1
            if graph[child]==0:
                queue.append(child)
    return res


def main():
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()

