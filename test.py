import string
import re
import tkinter as tk
from tkinter import messagebox


def load_common_passwords(filename="wordlist.txt"):
    try:
        return {line.strip() for line in open(filename, "r", encoding="utf-8")}
    except FileNotFoundError:
        print("Warning: 'wordlist.txt' not found. Skipping common password check.")
        return set()


def check_password_strength(password):
    min_length = 12  # NIST Standard
    upper = any(char in string.ascii_uppercase for char in password)
    lower = any(char in string.ascii_lowercase for char in password)
    digit = any(char in string.digits for char in password)
    special = any(char in string.punctuation for char in password)

    strength_score = sum([upper, lower, digit, special])
    
   
    common_passwords = load_common_passwords()

    if password in common_passwords:
        return "Critical Risk: Password is commonly used!"

    if len(password) < min_length:
        return "Weak: Password must be at least 12 characters long."

    if strength_score < 3:
        return "Moderate: Use at least three types (uppercase, lowercase, numbers, symbols)."

    return "Strong: Your password is secure."


def evaluate_password():
    password = password_entry.get()
    result = check_password_strength(password)
    messagebox.showinfo("Password Strength", result)

app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("400x250")
app.configure(bg='#ADD8E6')

tk.Label(app, text="Enter your password:", font=("Arial", 12), bg='#ADD8E6').pack(pady=10)
password_entry = tk.Entry(app, show='', width=50)
password_entry.pack(pady=5)

submit_btn = tk.Button(app, text="Check Password", command=evaluate_password, font=("Arial", 12), bg='#87CEEB', fg='white')
submit_btn.pack(pady=20)

app.mainloop()
