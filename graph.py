
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        print("BFS Traversal: ", end="")

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print()

    def dfs(self, start):
        visited = set()

        print("DFS Traversal: ", end="")

        def visit(vertex):
            visited.add(vertex)
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        print()


if __name__ == "__main__":
    name = input("Enter your name: ").strip().upper()

    if name:
        graph = Graph()

        # Connect each letter to the next letter
        for i in range(len(name) - 1):
            graph.add_edge(name[i], name[i + 1])

        print("\nGRAPH")
        graph.bfs(name[0])
        graph.dfs(name[0])
    else:
        print("Please enter a name.")
