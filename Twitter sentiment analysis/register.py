import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3  
import login 
import re


def validate_inputs(full_name, address, email, gender, mobile, username, password):
    """Validate registration inputs."""
    if not full_name or not full_name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Full Name must contain only letters and spaces.")
        return False
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email format.")
        return False
    if not gender:
        messagebox.showerror("Error", "Please select your gender.")
        return False
    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror("Error", "Mobile number must be a 10-digit number.")
        return False
    if not username:
        messagebox.showerror("Error", "Username cannot be empty.")
        return False
    if not password or len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long.")
        return False
    return True


def register_user(full_name, address, email, gender, mobile, username, password):
    
    if not validate_inputs(full_name, address, email, gender, mobile, username, password):
        return
    
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                address TEXT,
                email TEXT,
                gender TEXT,
                mobile TEXT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')

        cursor.execute('''
            INSERT INTO users (full_name, address, email, gender, mobile, username, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (full_name, address, email, gender, mobile, username, password))

        conn.commit()  
        conn.close()  

        messagebox.showinfo("Success", "Account created successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_registration_frame(root):
    for widget in root.winfo_children():
        widget.destroy()
        
    original_image = Image.open("2.jpg")
    resized_image = original_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(resized_image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(root, text="Twitter Sentiment Analysis", fg='black', bg="#cfd8dc", font=('Forte', 28), height=1, width=75).place(x=0, y=0)

    frame1= tk.Frame(root, height=50, width=460, bg="black")
    frame1.place(x=550, y=120)
    tk.Label(frame1, text="Registration Form", font=("Forte", 22), fg='white', bg='black').place(x=120, y=8)
    
    frame = tk.Frame(root, height=550, width=460, bg="#cfd8dc")
    frame.place(x=550, y=200)
    tk.Label(frame, text="Full Name:", font=("Times New Roman", 14), bg="#cfd8dc").place(x=80, y=50)
    full_name_entry = tk.Entry(frame, border=3, width=25, font=("Times New Roman", 14))
    full_name_entry.place(x=180, y=50, height=35)

    tk.Label(frame, text="Address:", font=("Times New Roman", 14), bg="#cfd8dc").place(x=80, y=100)
    address_entry = tk.Entry(frame, border=3, width=25, font=("Times New Roman", 14))
    address_entry.place(x=180, y=100, height=30)

    tk.Label(frame, text="Email:", font=("Times New Roman", 14), bg="#cfd8dc").place(x=80, y=150)
    email_entry = tk.Entry(frame, border=3, width=25, font=("Times New Roman", 14))
    email_entry.place(x=180, y=150, height=35)

    tk.Label(frame, text="Gender:", font=("Times New Roman", 14), bg="#cfd8dc").place(x=80, y=200)
    gender_var = tk.StringVar()
    gender_var.set("None") 
    tk.Radiobutton(frame, text="Male", font=("Times New Roman", 14), bg="#cfd8dc", value="Male", variable=gender_var).place(x=200, y=200)
    tk.Radiobutton(frame, text="Female", font=("Times New Roman", 14), bg="#cfd8dc", value="Female", variable=gender_var).place(x=320, y=200)

    tk.Label(frame, text="Mobile No:", font=("Times New Roman", 14), bg="#cfd8dc").place(x=80, y=250)
    mobile_entry = tk.Entry(frame, border=3, width=25, font=("Times New Roman", 14))
    mobile_entry.place(x=180, y=250, height=35)

    tk.Label(frame, text="Username:", font=("Times New Roman", 14), bg="#cfd8dc").place(x=80, y=300)
    username_entry = tk.Entry(frame, border=3, width=25, font=("Times New Roman", 14))
    username_entry.place(x=180, y=300, height=35)

    tk.Label(frame, text="Password:", font=("Times New Roman", 14), bg="#cfd8dc").place(x=80, y=350)
    password_entry = tk.Entry(frame, border=3, width=25, font=("Times New Roman", 14), show="*")
    password_entry.place(x=180, y=350, height=35)

    tk.Button(frame, text="Create Account", font=("Arial"), width=20, bg="black", fg="white",
              command=lambda: register_user(
                  full_name_entry.get(), address_entry.get(), email_entry.get(), 
                  gender_var.get(), mobile_entry.get(), username_entry.get(), password_entry.get()
              )).place(x=125, y=430)

    back_to_login = tk.Label(root, text="Already have an account? Login", font=("Times New Roman", 10), fg="blue", bg="#cfd8dc", cursor="hand2")
    back_to_login.place(x=690, y=680)
    back_to_login.bind("<Button-1>", lambda e: login.create_login_frame(root))  

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")  
    root.state('zoomed')
    show_registration_frame(root)
    root.mainloop()
