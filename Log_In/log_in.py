import tkinter as tk
from Log_In.Log_in_functions.log_in_validation import login_validation
from tkinter import messagebox

def log_in_page(root, switch_to_admin):
    def handle_login():
        email = email_entry.get()
        password = password_entry.get()
        result, role, employee_id = login_validation(email, password)  # Validate credentials
        if result:
            if role == "Admin":
                messagebox.showinfo("Login Successful", "You have successfully logged in!")
                # Navigate to Admin Dashboard
                switch_to_admin(root, employee_id)
            else:
                messagebox.showerror("Login Failed", "You don't have access to this part of the system.")
        else:
            messagebox.showerror("Login Failed", "Invalid email or password.")

    # UI Setup
    root.geometry("400x300")

    # Title Label
    title_label = tk.Label(root, text="Login to AMS", font=("Helvetica", 18, "bold"))
    title_label.pack(pady=20)

    # Email Label and Entry
    email_label = tk.Label(root, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(root, width=30)
    email_entry.pack()

    # Password Label and Entry
    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack()

    # Login Button
    login_button = tk.Button(root, text="Login", command=handle_login)
    login_button.pack(pady=20)

    root.mainloop()
