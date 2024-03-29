

# Depth first - goes to the depth of each node
# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

visited = set()  # Set to keep track of visited nodes.


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == '__main__':
    # Using a Python dictionary to act as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Driver Code
    dfs(visited, graph, 'A')
