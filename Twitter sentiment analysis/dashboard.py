from subprocess import call
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA  # principle categorical analysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from tkinter import messagebox
import subprocess
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

def open_dashboard(root):
    dashboard_root = tk.Tk()
    dashboard_root.title("Dashboard")
    tk.Label(dashboard_root, text="Welcome to the Dashboard", font=("Arial", 24)).pack(pady=20)
    dashboard_root.mainloop()
    
    
def Data_Preprocessing():
    data = pd.read_csv("tweets.csv")
    data = data.dropna()

    sentiment_mapping = {'positive': 1, 'negative': -1, 'neutral': 0}
    data['sentiment'] = data['sentiment'].map(sentiment_mapping)

    vectorizer = TfidfVectorizer(max_features=1000)
    x = vectorizer.fit_transform(data['text']).toarray()

    y = data['sentiment']

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.30, random_state=42)

    load = tk.Label(root, font=("Tempus sans ITC", 15, "bold"), width=50, height=1,
                    background="black", foreground="white",
                    text="Data Loaded => Splitted into 80% for training & 20% for Testing")
    load.place(x=570, y=100)


def Model_Training():
    data = pd.read_csv("tweets.csv")
    data = data.dropna()

    sentiment_mapping = {'positive': 1, 'negative': -1, 'neutral': 0}
    data['sentiment'] = data['sentiment'].map(sentiment_mapping)
   
    vectorizer = TfidfVectorizer(max_features=1000)
    x = vectorizer.fit_transform(data['text']).toarray()

    y = data['sentiment']
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.30, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy : %.2f%%" % (accuracy * 100.0))


    from joblib import dump
    dump(model, "RF_Model.joblib")
    dump(vectorizer, "vectorizer.joblib")
    print("Model saved as RF_Model.joblib")

    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))


    label4 = tk.Label(root, text=str(repo), width=45, height=10,
                      bg="#FFFDD0", fg="black", font=("ROBOTO", 14))
    label4.place(x=570, y=140)

    label5 = tk.Label(root, text="Accuracy : "+str(ACC)+"%\nModel saved as RF_Model.joblib",
                      width=45, height=5, bg="#FFFDD0", fg="black", font=("ROBOTO", 14))
    label5.place(x=570, y=350)
    

    rf_model = RandomForestClassifier()
    rf_model.fit(x_train, y_train)
    y_pred_rf = rf_model.predict(x_test)

    dt_model = DecisionTreeClassifier()
    dt_model.fit(x_train, y_train)
    y_pred_dt = dt_model.predict(x_test)

    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    accuracy_dt = accuracy_score(y_test, y_pred_dt)

    report_rf = classification_report(y_test, y_pred_rf)
    report_dt = classification_report(y_test, y_pred_dt)

    conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
    conf_matrix_dt = confusion_matrix(y_test, y_pred_dt)

    comparison_window = tk.Toplevel(root)
    comparison_window.title("Model Comparison")
    comparison_window.geometry("800x600")

    rf_label = tk.Label(comparison_window, text=f"Random Forest Accuracy: {accuracy_rf:.2f}",
                        font=("Arial", 14, "bold"), bg="#e3f2fd")
    rf_label.pack(pady=10)
    rf_report_label = tk.Label(comparison_window, text=f"Classification Report:\n{report_rf}",
                               font=("Arial", 12), bg="#e3f2fd", justify="left")
    rf_report_label.pack(pady=10)

    plt.figure(figsize=(4, 4))
    plt.matshow(conf_matrix_rf, cmap="coolwarm", fignum=1)
    for i in range(conf_matrix_rf.shape[0]):
        for j in range(conf_matrix_rf.shape[1]):
            plt.text(j, i, str(conf_matrix_rf[i, j]), ha="center", va="center")
    plt.title("Random Forest Confusion Matrix", pad=20)
    plt.savefig("rf_matrix.png")
    plt.close()

    rf_img = Image.open("rf_matrix.png")
    rf_img = rf_img.resize((250, 250))
    rf_photo = ImageTk.PhotoImage(rf_img)
    rf_canvas = tk.Label(comparison_window, image=rf_photo)
    rf_canvas.image = rf_photo
    rf_canvas.pack(pady=10)

    dt_label = tk.Label(comparison_window, text=f"Decision Tree Accuracy: {accuracy_dt:.2f}",
                        font=("Arial", 14, "bold"), bg="#ffebee")
    dt_label.pack(pady=10)
    dt_report_label = tk.Label(comparison_window, text=f"Classification Report:\n{report_dt}",
                               font=("Arial", 12), bg="#ffebee", justify="left")
    dt_report_label.pack(pady=10)

    plt.figure(figsize=(4, 4))
    plt.matshow(conf_matrix_dt, cmap="coolwarm", fignum=1)
    for i in range(conf_matrix_dt.shape[0]):
        for j in range(conf_matrix_dt.shape[1]):
            plt.text(j, i, str(conf_matrix_dt[i, j]), ha="center", va="center")
    plt.title("Decision Tree Confusion Matrix", pad=20)
    plt.savefig("dt_matrix.png")
    plt.close()

    dt_img = Image.open("dt_matrix.png")
    dt_img = dt_img.resize((250, 250), Image.LANCZOS)
    dt_photo = ImageTk.PhotoImage(dt_img)
    dt_canvas = tk.Label(comparison_window, image=dt_photo)
    dt_canvas.image = dt_photo
    dt_canvas.pack(pady=10)

    close_button = tk.Button(comparison_window, text="Close", font=("Arial", 14),
                             command=comparison_window.destroy)
    close_button.pack(pady=10)
    
    
    

def show_comparison():
    call(["python", "comparison.py"])
    


def check_prediction():
    call(["python", "prediction.py"])


def logout():
    root.destroy()
    subprocess.call(['python', 'home.py'])


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
                       font=("", 28, "bold"), fg="white", bg="#2c3e50")
title_label.place(x=0, y=0, width=w, height=70)


button_width = 300
button_height = 50
button_y_start = 100  
button_spacing = 20  

data_button = tk.Button(root, text="Data Preprocessing", font=("Arial", 18, "bold"),
                        bg="#bdc3c7", fg="black", command=Data_Preprocessing)
data_button.place(x=20, y=button_y_start,
                  width=button_width, height=button_height)

train_button = tk.Button(root, text="Model Training", font=("Arial", 18, "bold"),
                         bg="#bdc3c7", fg="black", command=Model_Training)
train_button.place(x=20, y=button_y_start + button_height + button_spacing,
                   width=button_width, height=button_height)

predict_button = tk.Button(root, text="Check Prediction", font=("Arial", 18, "bold"),
                           bg="#bdc3c7", fg="black", command=check_prediction)
predict_button.place(x=20, y=button_y_start + 2 * (button_height + button_spacing),
                     width=button_width, height=button_height)

compare_button = tk.Button(root, text="Show Comparison", font=("Arial", 18, "bold"),
                           bg="#bdc3c7", fg="black", command=show_comparison)
compare_button.place(x=20, y=button_y_start + 3 * (button_height + button_spacing),
                     width=button_width, height=button_height)


logout_button = tk.Button(root, text="Logout", font=("Arial", 18, "bold"),
                          bg="#bdc3c7", fg="black", command=logout)
logout_button.place(x=20, y=button_y_start + 4 * (button_height + button_spacing),
                    width=button_width, height=button_height)


root.mainloop()
