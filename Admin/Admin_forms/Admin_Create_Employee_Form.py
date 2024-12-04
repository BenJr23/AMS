import tkinter as tk
from tkinter import ttk
import sqlite3
import uuid
from DATABASEFUNCTION.Admin_Acc import hash_password
from DATABASEFUNCTION.Database_path_function import database_path_locator
from Admin.Admin_functions.Accounts_fetch import show_employee_table
from tkinter import messagebox


def creation_emp_form(user_id, table):
    def submit_form():
        """
        Handle form submission.
        Collects data from the form fields and processes it (e.g., save to a database).
        """
        fname = fname_entry.get()
        lname = lname_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        salt = uuid.uuid4().hex
        hashed_password = hash_password(password, salt)
        contact_no = contact_no_entry.get()
        role = role_combobox.get()
        createdby = user_id

        # Validate inputs (optional but recommended)
        if not fname or not lname or not email or not password or not contact_no or not role:
            print("All fields are required!")
            return
        if not role:
            messagebox.showwarning("Validation Error", "Please select a role.")
            return
        db_file = database_path_locator()
        conn = sqlite3.connect(db_file)

        try:
            # Perform database operation
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO EMPLOYEE (FName, LName, Email, Hashpassword, Hash, ContactNo, Role, CreatedBy)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (fname, lname, email, hashed_password, salt, contact_no, role, createdby))
            conn.commit()
            print("Employee added successfully!")
            # Clear the form after successful submission
            clear_form()
            show_employee_table(table)
            root.destroy()
        except sqlite3.IntegrityError as e:
            # Handle unique constraint violation or other integrity errors
            messagebox.showerror("Error", f"Could not add employee: {e}")
            return  # Cancel further execution of the function
        finally:
            conn.close()

    def cancel_form():
        """
        Clear the form fields and optionally close the window.
        """
        clear_form()
        root.destroy()
        print("Form canceled.")  # Optional: Add window close logic if desired

    def clear_form():
        """
        Clear all fields in the form.
        """
        fname_entry.delete(0, tk.END)
        lname_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        contact_no_entry.delete(0, tk.END)
        role_combobox.set('')

    root = tk.Tk()
    root.title("Employee Form")
    root.geometry("400x450")

    # Labels and Entry Widgets
    tk.Label(root, text="First Name:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    fname_entry = tk.Entry(root, font=("Helvetica", 12))
    fname_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Last Name:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
    lname_entry = tk.Entry(root, font=("Helvetica", 12))
    lname_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Email:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
    email_entry = tk.Entry(root, font=("Helvetica", 12))
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(root, text="Password:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
    password_entry = tk.Entry(root, font=("Helvetica", 12), show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Contact No:", font=("Helvetica", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
    contact_no_entry = tk.Entry(root, font=("Helvetica", 12))
    contact_no_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Role:", font=("Helvetica", 12)).grid(row=5, column=0, padx=10, pady=5, sticky="w")
    role_combobox = ttk.Combobox(root, values=["Cataloger", "Librarian", "Admin", "Staff"], font=("Helvetica", 12), state="readonly")
    role_combobox.grid(row=5, column=1, padx=10, pady=5)

    # Buttons for Submit and Cancel
    button_frame = tk.Frame(root)
    button_frame.grid(row=6, column=0, columnspan=2, pady=20)

    submit_button = tk.Button(button_frame, text="Submit", font=("Helvetica", 12), command=submit_form)
    submit_button.grid(row=0, column=0, padx=10)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Helvetica", 12), command=cancel_form)
    cancel_button.grid(row=0, column=1, padx=10)

# Run the application