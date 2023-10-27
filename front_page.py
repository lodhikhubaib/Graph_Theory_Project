import tkinter as tk
from PIL import Image, ImageTk
import importlib

class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Kruskal's Algorithm")

        # Load and display an image on the front page
        image = Image.open(r"C:\Users\HP\OneDrive\Desktop\Graph_Theory_Project\Graph_Theory_Project\src\b.png")  # Replace "front_page_image.jpg" with your image file
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
  
        
if __name__ == "__main__":
    root = tk.Tk()
    front_page = FrontPage(root)
    root.mainloop()
