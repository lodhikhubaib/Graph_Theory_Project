import tkinter as tk
from PIL import Image, ImageTk
import importlib
from tkinter import Canvas, messagebox

class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Kruskal's Algorithm")

        # Load and display an image on the front page
        image = Image.open(r"C:\Users\HP\OneDrive\Desktop\Graph_Theory_Project\Graph_Theory_Project\Kruskal Algorithms\src\front_page.jpg")  # Replace "front_page_image.jpg" with your image file
        image = image.resize((700, 500), Image.LANCZOS)  # Resize the image as per your requirement
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        self.image_label = tk.Label(root, image=photo)
        self.image_label.image = photo
        self.image_label.pack()

        # Add a title label
        title_label = tk.Label(root, text="Welcome to Kruskal's Algorithm", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20)

        # Add a start button
        start_button = tk.Button(root, text="Start", font=("Helvetica", 12, "bold"), command=self.start_algorithm)
        start_button.pack(pady=2)
        
    def start_algorithm(self):
        self.root.destroy()
        second_algo = importlib.import_module("second_page")
        second_page_instance = second_algo.SecondPage(tk.Tk())
        second_page_instance.root.mainloop()
        
    '''def on_close(self, event=None):
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
        
if __name__ == "__main__":
    root = tk.Tk()
    front_page = FrontPage(root)
    root.protocol("WM_DELETE_WINDOW", front_page.on_close)
    #FrontPage.root.protocol("WM_DELETE_WINDOW", FrontPage.on_close)
    root.mainloop()
