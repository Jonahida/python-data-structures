class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            print(f"Vertex {vertex} added.")
        else:
            print(f"Vertex {vertex} already exists.")
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)  # Assuming undirected graph
            print(f"Edge added between {vertex1} and {vertex2}.")
        else:
            print(f"One or both vertices not found.")
    
    def display(self):
        print("Graph:")
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")
