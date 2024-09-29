""" 
In computer science, a topological sort or topological ordering of a directed graph is a
linear ordering of its vertices such that for every directed edge (u,v) from vertex u to
 vertex v, u comes before v in the ordering.
 For instance, the vertices of the graph may represent tasks to be performed,
and the edges may represent constraints that one task must be performed before another;
in this application, a topological ordering is just a valid sequence for the tasks. Precisely,
a topological sort is a graph traversal in which each node v is visited only after all its dependencies are visited.
A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG). """ 


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited.add(v)

        # Visit all the neighbors
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.topological_sort_util(neighbor, visited, stack)

        # Push the vertex to the stack
        stack.append(v)

    def topological_sort(self):
        visited = set()
        stack = []

        # Use a list of vertices to avoid modifying the graph during iteration
        for vertex in list(self.graph.keys()):
            if vertex not in visited:
                self.topological_sort_util(vertex, visited, stack)

        # Return the reversed stack
        return stack[::-1]

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('D', 'F')

    result = g.topological_sort()
    print("Topological Sort:", result)
