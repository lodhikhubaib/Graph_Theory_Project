# Import tkinter module
import math
#import time
#import resource
import tkinter as tk
from PIL import Image, ImageTk
import importlib

# Define Graph class
class Graph:
    def __init__(self, vertices):
        self.V = vertices # Number of vertices
        self.graph = [] # List of edges

    # Add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        
    def remove_edge(self, u, v):
        for i in range(len(self.graph)):
            if self.graph[i][0] == u and self.graph[i][1] == v:
                del self.graph[i]
                break

    # Find the root of a vertex using union-find
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union two vertices using union-find
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Apply Kruskal's algorithm to find the MSF
    def kruskal(self):
        result = [] # List of edges in MSF
        i = 0 # Index for sorted edges
        e = 0 # Number of edges in MSF
        self.graph = sorted(self.graph, key=lambda item: item[2]) # Sort edges by weight
        parent = [] # List of roots for union-find
        rank = [] # List of ranks for union-find
        for node in range(self.V): # Initialize union-find
            parent.append(node)
            rank.append(0)
        while e < self.V - 1: # Loop until MSF is complete
            u, v, w = self.graph[i] # Get the next edge
            i += 1
            x = self.find(parent, u) # Find the roots of u and v
            y = self.find(parent, v)
            if x != y: # If they are not in the same component, add the edge to MSF
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y) # Union u and v
        return result


# Define GUI class
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        icon_image = tk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Graph_Theory_Project\Graph_Theory_Project\src\logo.png")
        self.window.iconphoto(True, icon_image)
        self.window.title("Kruskal's Algorithm")
        self.canvas = tk.Canvas(self.window, width=600, height=400)
        self.canvas.pack()
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(row=0, column=0)
        self.label1 = tk.Label(self.frame, text="Number of vertices")
        self.label1.grid(row=0, column=1)

        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(row=1, column=0)
        self.label2 = tk.Label(self.frame, text="Edge input (u,v,w)")
        self.label2.grid(row=1, column=1)

        self.entry3 = tk.Entry(self.frame)
        self.entry3.grid(row=2, column=0)
        self.label3 = tk.Label(self.frame, text="Remove Edge Input(u,v)")
        self.label3.grid(row=2, column=1)

        self.button1 = tk.Button(self.frame, text="Add edge", command=self.add_edge)
        self.button1.grid(row=3, column=0)
        self.button2 = tk.Button(self.frame, text="Remove edge", command=self.remove_edge)
        self.button2.grid(row=3, column=1)
        self.button3 = tk.Button(self.frame, text="Find MSF", command=self.find_msf)
        self.button3.grid(row=3, column=2)
        self.button4 = tk.Button(self.frame, text="Clear", command=self.clear)
        self.button4.grid(row=5, column=0)
        self.button5 = tk.Button(self.frame, text="Quit", command=self.quit)
        self.button5.grid(row=5, column=1)
        self.button5 = tk.Button(self.frame, text="Standard Graphs", command=self.Standard_graphs)
        self.button5.grid(row=5, column=2)
        self.button5 = tk.Button(self.frame, text="Disconnected Graph", command=self.Disconnected_graphs)
        self.button5.grid(row=7, column=0)
        self.graph = None
        self.coords = {}
        self.radius = 20
        
        #adding logo                 
        width, height = 200, 100
        original_image = Image.open(r"C:\Users\HP\OneDrive\Desktop\Gt Project\connected\logo1.png")
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(resized_image)
        logo_label = tk.Label(self.window, image=self.logo_image)
        logo_label.place(x=0, y=0)

    # Add an edge to the graph and draw it on the canvas
    
    def add_edge(self):
        edge = self.entry2.get() # Get the edge input
        if edge: # If not empty
            u, v, w = map(int, edge.split(",")) # Parse the edge input
            if not self.graph: # If graph is not initialized
                n = int(self.entry1.get()) # Get the number of vertices
                if n > 0: # If valid
                    self.graph = Graph(n) # Initialize graph object
                    self.draw_vertices() # Draw vertices on the canvas
            if self.graph: # If graph is initialized
                if 0 <= u < self.graph.V and 0 <= v < self.graph.V and w > 0: # If valid edge input
                    self.graph.add_edge(u, v, w) # Add edge to the graph
                    x1, y1 = self.coords[u] # Get the coordinates of u and v
                    x2, y2 = self.coords[v]
                    self.canvas.create_line(x1, y1, x2, y2) # Draw the edge on the canvas
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 # Get the midpoint of the edge
                    self.canvas.create_text(mx, my, text=str(w)) # Draw the weight on the canvas

    def remove_edge(self):
        edge = self.entry3.get()
        if edge:
            u, v = map(int, edge.split(","))
            if self.graph:
                if 0 <= u < self.graph.V and 0 <= v < self.graph.V:
                    self.graph.remove_edge(u, v)
                    self.canvas.delete("all")
                    self.draw_vertices()
                    for u, v, w in self.graph.graph:
                        x1, y1 = self.coords[u]
                        x2, y2 = self.coords[v]
                        self.canvas.create_line(x1, y1, x2, y2)
                        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                        self.canvas.create_text(mx, my, text=str(w))
    
    # Find the MSF using Kruskal's algorithm and highlight it on the canvas
    def find_msf(self):
        if self.graph: # If graph is initialized
            result = self.graph.kruskal() # Apply Kruskal's algorithm
            for u, v, w in result: # Loop through the edges in MSF
                x1, y1 = self.coords[u] # Get the coordinates of u and v
                x2, y2 = self.coords[v]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3) # Highlight the edge on the canvas

    # Clear the canvas and the graph
    def clear(self):
        self.canvas.delete("all") # Delete all items on the canvas
        self.graph = None # Reset graph object

    # Quit the program
    def quit(self):
        self.window.destroy() # Destroy main window

    def Standard_graphs(self):
        # Destroy the current window
        self.window.destroy()

        # Import the standard graph module
        standard_Graphs = importlib.import_module("Kruskal_Standard")

        # Create an instance of the standard graph GUI
        standard_gui = standard_Graphs.GUI()

        # Start the mainloop for the new GUI
        standard_gui.window.mainloop()

# for disconnected graphs
    def Disconnected_graphs(self):
        # Destroy the current window
        self.window.destroy()

        # Import the disconnected graph module
        Disconnected_Graphs = importlib.import_module("Disconnected")

        # Create an instance of the standard graph GUI
        disconnected_gui = Disconnected_Graphs.GUI()

        # Start the mainloop for the new GUI
        disconnected_gui.window.mainloop()

    '''    #for measuring execution time and memory usage for connected graphs
    def run_kruskal_connected(num_vertices, edges):
        graph = Graph(num_vertices)
        for u, v, weight in edges:
            graph.add_edge(u, v, weight)
        start_time = time.time()
        minimum_spanning_tree = graph.kruskal()
        end_time = time.time()
        execution_time = end_time - start_time
        memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024  # in kilobytes
        return execution_time, memory_usage

        execution_time, memory_usage = run_kruskal_connected(num_vertices, edges)
        print("Execution Time:", execution_time, "seconds")
        print("Memory Usage:", memory_usage, "KB")'''
        
    # Draw vertices on the canvas in a circular layout
    def draw_vertices(self):
        cx, cy = 300, 200 # Center of the circle
        r = 150 # Radius of the circle
        angle = 180 # Starting angle
        step = 360 / self.graph.V # Angle increment
        for i in range(self.graph.V): # Loop through vertices
            x = cx + r * math.cos(math.radians(angle)) # Calculate x coordinate using trigonometry
            y = cy + r * math.sin(math.radians(angle)) # Calculate y coordinate using trigonometry
            angle += step # Increment angle
            self.coords[i] = (x, y) # Store coordinates in dictionary
            self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius,
                                    fill="white")  # Draw vertex as a circle on the canvas
            self.canvas.create_text(x, y, text=str(i))  # Draw vertex label on the canvas

# Run GUI program
gui = GUI()
gui.window.mainloop()
