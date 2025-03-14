import tkinter as tk
from tkinter import Label, Frame, Button
from PIL import Image, ImageTk

def display_images(window, image_paths):
    for i, path in enumerate(image_paths):
        try:
            
            img = Image.open(path)
            
            img = img.resize((400, 300), Image.ANTIALIAS)
           
            photo = ImageTk.PhotoImage(img)
            
            label = Label(window, image=photo, bg="white")
            label.image = photo  

            label.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        except Exception as e:
            print(f"Error loading image {path}: {e}")


root = tk.Tk()
root.title("Twitter Sentiment Analysis")
root.geometry("900x600")
root.configure(bg="lightblue")


header = Frame(root, bg="darkblue", height=50)
header.pack(fill="x")
header_label = Label(header, text="Twitter Sentiment Analysis Dashboard", font=("Arial", 18, "bold"), fg="white", bg="darkblue")
header_label.pack(pady=10)


content_frame = Frame(root, bg="lightblue")
content_frame.pack(expand=True, fill="both", padx=20, pady=20)


image_paths = ["dt_matrix.png", "rf_matrix.png"]  # Replace with actual file paths


display_images(content_frame, image_paths)


footer = Frame(root, bg="darkblue", height=30)
footer.pack(fill="x", side="bottom")
footer_label = Label(footer, text="- Twitter Sentiment Analysis", font=("Arial", 10), fg="white", bg="darkblue")
footer_label.pack(pady=5)


root.mainloop()
