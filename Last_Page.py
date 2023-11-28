import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

def load_and_display_image(image_path, canvas):
    try:
        image = PhotoImage(file=image_path)
        # Centering the image on the canvas
        x = (canvas.winfo_reqwidth() - image.width()) / 2
        y = (canvas.winfo_reqheight() - image.height()) / 2
        canvas.create_image(x, y, anchor=tk.NW, image=image)
        canvas.image = image  # Keep a reference to the image to prevent it from being garbage collected
    except Exception as e:
        print("Error loading image:", e)

def create_canvas_with_details(window, frame, row, column, details_text, image_path):
    # Picture canvas
    canvas = tk.Canvas(frame, width=300, height=400, bg="white", bd=0, highlightthickness=0)
    canvas.grid(row=row, column=column, padx=12, pady=12)

    # Load and display the image on the canvas
    load_and_display_image(image_path, canvas)

    # Details canvas
    details_canvas = tk.Canvas(frame, width=300, height=100, bg="black", bd=0, highlightthickness=0)
    details_canvas.grid(row=row + 1, column=column, padx=12, pady=6)

    # Developer details labels
    details_label = tk.Label(details_canvas, text=details_text, justify=tk.LEFT, bg="white", fg="black", highlightthickness=0)
    details_label.grid(row=0, column=0, pady=(0, 0), sticky=tk.W)  # Removed top padding to eliminate the gap

def on_last_page_close():
    # Function to be called when the user closes the last page
    messagebox.showinfo("Last Page", "This is the last page for developers. Thank You for Using this Application!!")
    print("Tkinter application closed.")
    # You can add more logic here before closing the application
    root.destroy()

root = tk.Tk()
root.title("Kruskal Algorithm")
root.configure(bg="white")

# Set the window size to the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Main frame
main_frame = tk.Frame(root, bg="white")
main_frame.grid(row=0, column=0, padx=12, pady=12)

# Developer-specific content
developer_content = """
Welcome, Developer!

Thank you for using our application.

Here is the Information Of the Developer!
"""

label = tk.Label(main_frame, text=developer_content, bg="white")
label.grid(padx=12, pady=12)

# Create six canvas widgets
aahail_image_path = r"C:\Users\HP\OneDrive\Desktop\algo\Line inte\Tkinter\aahail.ppm" # Replace with the actual path to the image
khuzaima_image_path = r"C:\Users\HP\OneDrive\Desktop\algo\Line inte\Tkinter\khuzaima.ppm"# Replace with the actual path to the image
khubaib_image_path = r"C:\Users\HP\OneDrive\Desktop\algo\Line inte\Tkinter\khubaib.ppm"  # Replace with the actual path to the image

aahail_details = "Name: Aahil Ashiq Ali\nEmail: aahilashiqali@gmail.com\nLinkedIn: Aahil Ashiq Ali\nUniversity: FAST NUCES, Karachi"
khubaib_details = "Name: Muhammad Khubaib Khan Lodhi\nEmail: lodhikhubaib12@gmail.com\nLinkedIn: Khubaib Lodhi\nUniversity: FAST NUCES, Karachi"
khuzaima_details = "Name: Khuzaima Ahsan\nEmail: khuzaimaahsan07@gmail.com\nLinkedIn: KHUZAIMA AHSAN\nUniversity: FAST NUCES, Karachi"

create_canvas_with_details(root, main_frame, 1, 0, khuzaima_details, khuzaima_image_path)
create_canvas_with_details(root, main_frame, 1, 1, khubaib_details, khubaib_image_path)
create_canvas_with_details(root, main_frame, 1, 2, aahail_details, aahail_image_path)

# Bind the close event to the on_last_page_close function
root.protocol("WM_DELETE_WINDOW", on_last_page_close)

root.mainloop()
