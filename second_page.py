from PIL import Image, ImageTk
import tkinter as tk
import importlib
from tkinter import Canvas, messagebox

class SecondPage:
    def __init__(self, root, displayed=False):
        self.root = root
        self.root.title("Kruskal's Algorithm")
        self.root.geometry(f"{1000}x{1000}")
        self.displayed = displayed  # Flag to indicate if the page has been displayed

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the new width and height for the image (80% of the screen width and height)
        image_width = int(0.9 * screen_width)
        image_height = int(0.9 * screen_height)

        # Load the background image and resize it
        background_image = Image.open(r"C:\Users\HP\OneDrive\Desktop\Graph_Theory_Project\Graph_Theory_Project\src\ivv.png")
        image = background_image.resize((image_width, image_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the resized background image
        self.image_label = tk.Label(root, image=photo)
        self.image_label.image = photo
        self.image_label.place(x=screen_width // 4 - image_width // 4, y=screen_height // 4 - image_height // 4)  # Center the image on the screen

        # Create buttons with appropriate spacing
        button_spacing = 60  # Adjust the spacing between buttons as needed

        # Button for Minimum Spanning Tree
        min_span_tree_button = tk.Button(root, text="Minimum Spanning Tree", command=self.Min_Spanning_algorithm, font=("Helvetica", 18, "bold"))
        min_span_tree_button.place(x=screen_width // 4, y=screen_height // 4 + image_height // 4 + button_spacing, anchor="w")

        # Button for Maximum Spanning Tree
        max_span_tree_button = tk.Button(root, text="Maximum Spanning Tree", command=self.Max_Spanning_algorithm, font=("Helvetica", 18, "bold"))
        max_span_tree_button.place(x=screen_width // 4, y=screen_height // 4 + image_height // 4 + 2 * button_spacing, anchor="w")

        # Button for Minimum Spanning Tree for Disconnected Graph
        min_span_tree_dis_button = tk.Button(root, text="Minimum Spanning Tree for Disconnected Graph", command=self.Min_Spanning_algorithm_dis, font=("Helvetica", 18, "bold"))
        min_span_tree_dis_button.place(x=screen_width // 4, y=screen_height // 4 + image_height // 4 + 3 * button_spacing, anchor="w")

        # Register the on_close method for the window closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def Min_Spanning_algorithm(self):
        if not self.displayed:  # Check if the page has been displayed
            self.displayed = True  # Set the flag to True
            self.root.destroy()  # Destroy the current page
            start_algo = importlib.import_module("Kruskal_Algorithm")
            start_gui = start_algo.GUI()
            start_gui.window.mainloop()

    def Max_Spanning_algorithm(self):
        if not self.displayed:  # Check if the page has been displayed
            self.displayed = True  # Set the flag to True
            self.root.destroy()  # Destroy the current page
            start_algo = importlib.import_module("Maximium_spanning")
            start_gui = start_algo.GUI()
            start_gui.window.mainloop()

    def Min_Spanning_algorithm_dis(self):
        if not self.displayed:  # Check if the page has been displayed
            self.displayed = True  # Set the flag to True
            self.root.destroy()  # Destroy the current page
            start_algo = importlib.import_module("Disconnected")
            start_gui = start_algo.GUI()
            start_gui.window.mainloop()
            
    '''def on_close(self):
        # Prompt the user with a Yes/No messagebox
        user_response = messagebox.askyesno("Confirmation", "Do you want to close the application?")
        if user_response:
            print("Tkinter application closed.")
            self.root.destroy()'''
    
    def on_close(self):
    # Prompt the user with a Yes/No messagebox
        user_response = messagebox.askyesno("Confirmation", "Do you want to close the application?")
        if user_response:
            print("Tkinter application closed.")
        # Hide the current window (assuming it's the 'window' variable from the previous code)
            #self.window.iconify()
            self.root.destroy()
        # Open a new application or perform other actions
            self.End_program()

    def End_program(self):
        #window.destroy()
        last_page = importlib.import_module("Last_Page")
        #last_page_gui = last_page.GUI()
        #last_page_gui.window.mainloop()



# Run the Tkinter main loop
if __name__ == "__main__":
    root = tk.Tk()
    second_page = SecondPage(root)
    root.mainloop()
