import tkinter as tk
from PIL import Image, ImageTk
import login
import register


def open_login():
    login.create_login_frame(root)  

def open_register():
    register.show_registration_frame(root)  

root = tk.Tk()
root.title("Twitter Sentiment Analysis")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}")
root.state('zoomed')

bg_image = Image.open("2.jpg")  
bg_image = bg_image.resize((w, h), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


title_label = tk.Label(root, text="Twitter Sentiment Analysis", 
                       font=("Edwardian Script ITC", 50, "bold"), fg="white", bg="#19547b")
title_label.place(x=0, y=0, width=w, height=60)

button_frame = tk.Frame(root, bg="#ffffff", relief="raised", bd=5)
button_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=200)


login_button = tk.Button(button_frame, text="Login", font=("Arial", 18, "bold"), 
                         bg="#0078d7", fg="white", command=open_login)
login_button.pack(pady=20, fill="x", padx=20)


register_button = tk.Button(button_frame, text="Register", font=("Arial", 18, "bold"), 
                            bg="#28a745", fg="white", command=open_register)
register_button.pack(pady=20, fill="x", padx=20)

root.mainloop()
