import tkinter as tk
from tkinter import ttk
from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer


def Detect():
    t1 = text.get()

    try:
        
        model = load("RF_Model.joblib")
        vectorizer = load("vectorizer.joblib")  

        t1_transformed = vectorizer.transform([t1]).toarray()

        sentiment_mapping = model.predict(t1_transformed)

        if sentiment_mapping == 1:
            result_label.config(text="Positive Sentiment", bg="green", fg="white")
        elif sentiment_mapping == -1:
            result_label.config(text="Negative Sentiment", bg="red", fg="white")
        elif sentiment_mapping == 0:
            result_label.config(text="Neutral Sentiment", bg="blue", fg="white")
        else:
            result_label.config(text="Unknown Sentiment", bg="black", fg="white")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", bg="yellow", fg="black")


root = tk.Tk()
root.title("Tweet Sentiment Analysis")
root.geometry("600x400")
root.configure(bg="lightblue")


title_label = tk.Label(root, text="Tweet Sentiment Analysis", font=("Arial", 20, "bold"), bg="black", fg="white")
title_label.pack(fill="x")

text = tk.StringVar()
fields = [
    ("text", text),
    
]


input_frame = tk.Frame(root, bg="lightblue")
input_frame.pack(pady=20)

input_label = tk.Label(input_frame, text="Enter Tweet Text:", font=("Arial", 14), bg="lightblue")
input_label.grid(row=0, column=0, padx=10, pady=5)

input_entry = ttk.Entry(input_frame, textvariable=text, font=("Arial", 14), width=30)
input_entry.grid(row=0, column=1, padx=10, pady=5)



predict_button = tk.Button(root, text="Analyze", command=Detect, font=("Arial", 16, "bold"), bg="green", fg="white")
predict_button.pack(pady=20)


result_label = tk.Label(root, text="", font=("Arial", 16), width=30, height=2, bg="lightblue", fg="black")
result_label.pack(pady=10)

root.mainloop()
