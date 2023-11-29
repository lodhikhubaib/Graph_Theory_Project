import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    edges = []
    while True:
        edge_input = input("Enter edge as 'u v weight' (or press Enter to finish): ")
        if not edge_input:
            break
        u, v, weight = map(int, edge_input.replace(',', ' ').split())  # Replace commas with spaces and then split
        edges.append((u, v, weight))
    return edges

class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskal(self):
        self.graph.sort(key=lambda x: x[2])
        parent = {}
        rank = {}

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_u] = root_v
                    if rank[root_u] == rank[root_v]:
                        rank[root_v] += 1

        minimum_spanning_trees = []
        visited = set()
        for u, v, w in self.graph:
            if u not in parent:
                parent[u] = u
                rank[u] = 0
            if v not in parent:
                parent[v] = v
                rank[v] = 0

            if find(u) != find(v):
                union(u, v)
                visited.add(u)
                visited.add(v)
                minimum_spanning_trees.append((u, v, w))

        # Add isolated vertices to the minimum spanning trees
        isolated_vertices = set(parent.keys()) - visited
        for vertex in isolated_vertices:
            minimum_spanning_trees.append((vertex, vertex, 0))

        return minimum_spanning_trees

# Get user input for graph edges
edges = create_graph()

# Create a graph from user input
user_graph = nx.Graph()
user_graph.add_weighted_edges_from(edges)

# Find minimum spanning trees for each connected component using Kruskal's algorithm
graph = Graph()
for edge in user_graph.edges(data=True):
    u, v, w = edge
    graph.add_edge(u, v, w['weight'])

minimum_spanning_trees = graph.kruskal()
print("Minimum Spanning Trees (Kruskal's Algorithm):", minimum_spanning_trees)

# Draw the user input graph and minimum spanning trees
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(user_graph)  # Positioning the nodes using spring layout
edge_labels={(u, v): d['weight'] for u, v, d in user_graph.edges(data=True)}
nx.draw(user_graph, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=15, font_weight='bold')
nx.draw_networkx_edges(user_graph, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edge_labels(user_graph,pos,edge_labels=edge_labels, font_size=10)

for tree in minimum_spanning_trees:
    u, v, _ = tree
    nx.draw_networkx_edges(user_graph, pos, edgelist=[(u, v)], width=2.0, edge_color='red')

plt.title("User Input Graph with Minimum Spanning Trees")
plt.show()