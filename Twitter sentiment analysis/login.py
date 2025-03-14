import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3
import register
import subprocess



def create_login_frame(root):
    for widget in root.winfo_children():
        widget.destroy()

    original_image = Image.open("2.jpg")  
    resized_image = original_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(resized_image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_label = tk.Label(
        root, text="Twitter Sentiment Analysis",
        font=("Forte", 30), bg='#004e92', fg='black', pady=5
    )
    title_label.place(x=0, y=0, width=root.winfo_screenwidth())

    login_label = tk.Label(root, text="Admin Login", font=("Times New Roman", 18, "bold"), bg='#12beff', fg='black')
    login_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER, width=350, height=50)

    auth_frame = tk.Frame(root, bg='#cfd8dc')
    auth_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=350, height=300)

    tk.Label(auth_frame, text="Username:", font=("Times New Roman", 14), bg='#cfd8dc', fg='black').grid(row=0, column=0, padx=20, pady=20)
    username = tk.StringVar()
    tk.Entry(auth_frame, textvariable=username, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, padx=20, pady=20)

    tk.Label(auth_frame, text="Password:", font=("Times New Roman", 14), bg='#cfd8dc', fg='black').grid(row=1, column=0, padx=20, pady=20)
    password = tk.StringVar()
    tk.Entry(auth_frame, textvariable=password, font=("Times New Roman", 14), relief='solid', show="*").grid(row=1, column=1, padx=20, pady=20)

    tk.Button(
        auth_frame, text="Login", command=lambda: login(username, password, root),
        font=("Times New Roman", 18), fg="Black", bg='#2be040', relief='raised'
    ).grid(row=2, column=0, columnspan=2, pady=30)

    register_label = tk.Label(
        auth_frame, text="Don't have an account? Register", font=("Times New Roman", 10),
        fg="blue", bg="#cfd8dc", cursor="hand2"
    )
    register_label.grid(row=4, column=0, columnspan=2)
    register_label.bind("<Button-1>", lambda e: show_registration_frame(root))


def login(username, password, root):
    if not username.get() or not password.get():
        ms.showerror("Error", "Username and Password cannot be empty.")
        return

    with sqlite3.connect('users.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username.get(), password.get()))
        if cursor.fetchone():
            root.destroy() 
            import dashboard
            dashboard.show_dashboard
        else:
            ms.showerror("Error", "Invalid Username or Password.")
  

def show_registration_frame(root):
    register.show_registration_frame(root)
    



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.state('zoomed')
    create_login_frame(root)
    root.mainloop()
