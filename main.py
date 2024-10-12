import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store passwords
PASSWORD_FILE = 'passwords.json'

# Function to load passwords from the file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save passwords to the file
def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file:
        json.dump(passwords, file, indent=4)

# Function to add a new password
def add_password():
    site = site_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if site and username and password:
        passwords[site] = {"username": username, "password": password}
        save_passwords(passwords)
        update_password_list()
        site_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Function to delete a password
def delete_password(site):
    if site in passwords:
        del passwords[site]
        save_passwords(passwords)
        update_password_list()

# Function to update the displayed password list
def update_password_list():
    for widget in password_frame.winfo_children():
        widget.destroy()

    for site, details in passwords.items():
        frame = tk.Frame(password_frame)
        frame.pack(fill='x', pady=5)

        site_label = tk.Label(frame, text=f"Site: {site}", anchor='w')
        site_label.pack(side='left', expand=True, fill='x')

        username_label = tk.Label(frame, text=f"Username: {details['username']}", anchor='w')
        username_label.pack(side='left', expand=True, fill='x')

        password_label = tk.Label(frame, text=f"Password: {details['password']}", anchor='w')
        password_label.pack(side='left', expand=True, fill='x')

        delete_button = tk.Button(frame, text="Delete", command=lambda s=site: delete_password(s))
        delete_button.pack(side='right')

# GUI setup
root = tk.Tk()
root.title("Cryptic Password Manager")
root.geometry('500x400')
root.configure(bg='#f5f5f5')

# Global dictionary to hold passwords
passwords = load_passwords()

# Header
header = tk.Label(root, text="Cryptic Password Manager", font=('Arial', 18, 'bold'), bg='#f5f5f5', fg='#333')
header.pack(pady=10)

# Add password section
form_frame = tk.Frame(root, bg='#f5f5f5')
form_frame.pack(pady=10)

site_label = tk.Label(form_frame, text="Website:", bg='#f5f5f5')
site_label.grid(row=0, column=0, padx=10, pady=5)
site_entry = tk.Entry(form_frame, width=30)
site_entry.grid(row=0, column=1, padx=10, pady=5)

username_label = tk.Label(form_frame, text="Username:", bg='#f5f5f5')
username_label.grid(row=1, column=0, padx=10, pady=5)
username_entry = tk.Entry(form_frame, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_label = tk.Label(form_frame, text="Password:", bg='#f5f5f5')
password_label.grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(form_frame, width=30)
password_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Password", command=add_password, bg='#3498db', fg='white', width=20)
add_button.pack(pady=10)

# Password list section
password_frame = tk.Frame(root, bg='#f5f5f5')
password_frame.pack(pady=10, fill='both', expand=True)

# Load and display existing passwords
update_password_list()

root.mainloop()
