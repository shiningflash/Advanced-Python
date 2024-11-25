from typing import List


class Graph:
    def __init__(self, node_count: int) -> None:
        self.node_count = node_count
        self.graph = [[] for _ in range(node_count)]
        self.visited = [False for _ in range(node_count)]
    
    def addEdge(self, u: int, v: int) -> None:
        # validation
        if not (0 <= u < self.node_count and 0 <= v < self.node_count):
            raise ValueError(f'Invalid node: {u}, {v}')
        
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, node: int) -> None:
        stack = [node]
        self.visited[node] = True
        while stack:
            node = stack.pop()
            for child in self.graph[node]:
                if not self.visited[child]:
                    self.visited[child] = True
                    stack.append(child)

    def countTrees(self) -> int:
        count = 0
        for node in range(self.node_count):
            if not self.visited[node]:
                self.dfs(node)
                count += 1
        return count


if __name__ == '__main__':
    node_count = 5
    graph = Graph(node_count)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(3, 3)
    print(graph.countTrees())
    