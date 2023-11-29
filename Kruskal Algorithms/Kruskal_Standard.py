import tkinter as tk
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Function to generate a graph based on user input
def generate_graph(graph_type, num_nodes):
    if graph_type == 'complete':
        graph = nx.complete_graph(num_nodes)
    elif graph_type == 'path':
        graph = nx.path_graph(num_nodes)
    elif graph_type == 'wheel':
        graph = nx.wheel_graph(num_nodes)
    elif graph_type == 'cycle':
        graph = nx.cycle_graph(num_nodes)
    else:
        print("Invalid graph type!")
        return None

    # Get edge weights from the user
    for u, v in graph.edges():
        weight = float(input(f"Enter weight for edge {u}-{v}: "))
        graph[u][v]['weight'] = weight

    return graph

# Function to apply Kruskal's algorithm to find minimum spanning tree
# ... (same as before)
def kruskal_minimum_spanning_tree(graph):
    edges = list(graph.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])
    mst_edges = []
    disjoint_sets = [{node} for node in graph.nodes()]

    for edge in edges:
        u, v, weight = edge
        u_set, v_set = None, None
        for subset in disjoint_sets:
            if u in subset:
                u_set = subset
            if v in subset:
                v_set = subset
        if u_set != v_set:
            mst_edges.append((u, v, weight))
            disjoint_sets.remove(u_set)
            disjoint_sets.remove(v_set)
            disjoint_sets.append(u_set.union(v_set))

    mst_graph = nx.Graph()
    mst_graph.add_edges_from(mst_edges)
    return mst_graph
    # ... (same as before)
    
def calculate_total_weight(graph):
    total_weight = sum(edge[2]['weight'] for edge in graph.edges(data=True))
    return total_weight

# Function to create and visualize the graph based on user input
def create_and_visualize_graph():
    graph_type = entry_graph_type.get().lower()
    num_nodes = int(entry_num_nodes.get())
    graph = generate_graph(graph_type, num_nodes)

    if graph:
        print("Graph:")
        print(graph.edges())
        minimum_spanning_forest = kruskal_minimum_spanning_tree(graph)
        total_weight = calculate_total_weight(minimum_spanning_forest)
        print(f"Total Weight of Minimum Spanning Tree: {total_weight}")
        draw_graph(graph)
        draw_minimum_spanning_tree(minimum_spanning_forest)
    else:
        print("Invalid graph type!")

# Function to draw the graph
def draw_graph(graph_to_draw):
    plt.clf()
    fig, ax = plt.subplots()
    pos = nx.spring_layout(graph_to_draw)
    edge_labels = {(u, v): d['weight'] for u, v, d in graph_to_draw.edges(data=True)}
    nx.draw(graph_to_draw, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold', width=2, edge_color='gray', ax=ax)
    nx.draw_networkx_edge_labels(graph_to_draw, pos, edge_labels=edge_labels, font_color='red')
    ax.set_axis_off()
    canvas.draw()

# Function to draw the minimum spanning tree
def draw_minimum_spanning_tree(tree):
    fig, ax = plt.subplots()
    pos = nx.spring_layout(tree)
    edge_labels = {(u, v): d['weight'] for u, v, d in tree.edges(data=True)}
    nx.draw(tree, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold', width=2, edge_color='green', ax=ax)
    nx.draw_networkx_edge_labels(tree, pos, edge_labels=edge_labels, font_color='red')
    ax.set_title("Minimum Spanning Tree")
    plt.show()

# GUI using tkinter and networkx
root = tk.Tk()
root.title("Minimum Spanning Forest")

# Entry for graph type (complete, path, wheel, cycle)
tk.Label(root, text="Enter graph type (complete, path, wheel, cycle):").pack()
entry_graph_type = tk.Entry(root)
entry_graph_type.pack()

# Entry for number of nodes
tk.Label(root, text="Enter number of nodes:").pack()
entry_num_nodes = tk.Entry(root)
entry_num_nodes.pack()

# Button to create and visualize the graph
create_button = tk.Button(root, text="Create and Visualize Graph", command=create_and_visualize_graph)
create_button.pack()

# Canvas for drawing the graph
canvas = FigureCanvasTkAgg(plt.figure(), master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

root.mainloop()
