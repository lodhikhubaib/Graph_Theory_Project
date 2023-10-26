import tkinter as tk
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

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

    for u, v in graph.edges():
        weight = float(input(f"Enter weight for edge {u}-{v}: "))
        graph[u][v]['weight'] = weight

    return graph

def reverse_weights(graph):
    reversed_graph = graph.copy()
    for u, v in reversed_graph.edges():
        reversed_graph[u][v]['weight'] = -reversed_graph[u][v]['weight']
    return reversed_graph

def calculate_total_weight(graph):
    total_weight = sum(abs(edge[2]['weight']) for edge in graph.edges(data=True))
    return total_weight

def create_and_visualize_graph():
    graph_type = entry_graph_type.get().lower()
    num_nodes = int(entry_num_nodes.get())
    graph = generate_graph(graph_type, num_nodes)

    if graph:
        print("Graph:")
        print(graph.edges())
        reversed_graph = reverse_weights(graph)
        maximum_spanning_tree = kruskal_maximum_spanning_tree(reversed_graph)
        total_weight = calculate_total_weight(maximum_spanning_tree)
        print(f"Total Weight of Maximum Spanning Tree: {total_weight}")
        draw_graph(graph)
        draw_maximum_spanning_tree(maximum_spanning_tree)
    else:
        print("Invalid graph type!")

def kruskal_maximum_spanning_tree(graph):
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

def draw_graph(graph_to_draw):
    plt.clf()
    fig, ax = plt.subplots()
    pos = nx.spring_layout(graph_to_draw)
    edge_labels = {(u, v): d['weight'] for u, v, d in graph_to_draw.edges(data=True)}
    nx.draw(graph_to_draw, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold', width=2, edge_color='gray', ax=ax)
    nx.draw_networkx_edge_labels(graph_to_draw, pos, edge_labels=edge_labels, font_color='red')
    ax.set_axis_off()
    canvas.draw()

def draw_maximum_spanning_tree(tree):
    fig, ax = plt.subplots()
    pos = nx.spring_layout(tree)
    edge_labels = {(u, v): d['weight'] for u, v, d in tree.edges(data=True)}
    nx.draw(tree, pos, with_labels=True, node_size=700, node_color='green', font_size=12,font_weight='bold', width=2, edge_color='green', ax=ax)
    nx.draw_networkx_edge_labels(tree, pos, edge_labels=edge_labels, font_color='red')
    ax.set_title("Maximum Spanning Tree")
    plt.show()

root = tk.Tk()
root.title("Maximum Spanning Tree")

tk.Label(root, text="Enter graph type (complete, path, wheel, cycle):").pack()
entry_graph_type = tk.Entry(root)
entry_graph_type.pack()

tk.Label(root, text="Enter number of nodes:").pack()
entry_num_nodes = tk.Entry(root)
entry_num_nodes.pack()

create_button = tk.Button(root, text="Create and Visualize Graph", command=create_and_visualize_graph)
create_button.pack()

canvas = FigureCanvasTkAgg(plt.figure(), master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

root.mainloop()
