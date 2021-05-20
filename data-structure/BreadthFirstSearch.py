
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

visited = []  # List to keep track of visited nodes.
queue = []     # Initialize a queue


# Traverse through nodes from left to right
# Check the following link https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
      # Driver Code
      bfs(visited, graph, 'A')