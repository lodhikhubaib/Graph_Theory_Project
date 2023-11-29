import math
import tkinter as tk
import importlib
from PIL import Image, ImageTk

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def remove_edge(self, u, v):
        for i in range(len(self.graph)):
            if self.graph[i][0] == u and self.graph[i][1] == v:
                del self.graph[i]
                break
            
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

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

    def maximum_spanning_tree(self):
        result = []
        i = 0
        self.graph = sorted(self.graph, key=lambda item: item[2], reverse=True)
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        while len(result) < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return result

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        icon_image = tk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Graph_Theory_Project\Graph_Theory_Project\Kruskal Algorithms\src\logo.png")
        self.window.iconphoto(True, icon_image)
        self.window.title("Maximum Spanning Tree")
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
        self.button2 = tk.Button(self.frame, text="Find MST", command=self.find_mst)
        self.button2.grid(row=3, column=2)
        self.button3 = tk.Button(self.frame, text="Clear", command=self.clear)
        self.button3.grid(row=5, column=0)
        self.button4 = tk.Button(self.frame, text="Quit", command=self.quit)
        self.button4.grid(row=5, column=1)
        self.button4 = tk.Button(self.frame, text="Standard Graphs", command=self.Standard_graphs)
        self.button4.grid(row=5, column=3)
        

        self.graph = None
        self.coords = {}
        self.radius = 20
        
        #adding logo                 
        width, height = 200, 100
        original_image = Image.open(r"C:\Users\HP\OneDrive\Desktop\Graph_Theory_Project\Graph_Theory_Project\Kruskal Algorithms\src\logo1.png")
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(resized_image)
        logo_label = tk.Label(self.window, image=self.logo_image)
        logo_label.place(x=0, y=0)

        

    def add_edge(self):
        edge = self.entry2.get()
        if edge:
            u, v, w = map(int, edge.split(","))
            if not self.graph:
                n = int(self.entry1.get())
                if n > 0:
                    self.graph = Graph(n)
                    self.draw_vertices()
            if self.graph:
                if 0 <= u < self.graph.V and 0 <= v < self.graph.V and w > 0:
                    self.graph.add_edge(u, v, w)
                    x1, y1 = self.coords[u]
                    x2, y2 = self.coords[v]
                    self.canvas.create_line(x1, y1, x2, y2)
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    self.canvas.create_text(mx, my, text=str(w))

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

    def find_mst(self):
        if self.graph:
            result = self.graph.maximum_spanning_tree()
            for u, v, w in result:
                x1, y1 = self.coords[u]
                x2, y2 = self.coords[v]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

    def clear(self):
        self.canvas.delete("all")
        self.graph = None

    def quit(self):
        self.window.destroy()

    def Standard_graphs(self):
        # Destroy the current window
        self.window.destroy()

        # Import the standard graph module
        standard_Graphs = importlib.import_module("Maximium_Spanning_Tree")

        # Create an instance of the standard graph GUI
        standard_gui = standard_Graphs.GUI()

        # Start the mainloop for the new GUI
        standard_gui.window.mainloop()
        
    def draw_vertices(self):
        cx, cy = 300, 200
        r = 150
        angle = 180
        step = 360 / self.graph.V
        for i in range(self.graph.V):
            x = cx + r * math.cos(math.radians(angle))
            y = cy + r * math.sin(math.radians(angle))
            angle += step
            self.coords[i] = (x, y)
            self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius,
                                    fill="white")
            self.canvas.create_text(x, y, text=str(i))

gui = GUI()
gui.window.mainloop()
