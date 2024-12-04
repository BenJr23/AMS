import tkinter as tk
from tkinter import ttk
import sqlite3
from DATABASEFUNCTION.Database_path_function import database_path_locator
from Admin.Admin_functions.Accounts_fetch import show_employee_table
from tkinter import messagebox


def edit_emp_form(user_id, table, selected_employee_id):
    def populate_form():
        """
        Fetch employee data by employee_id and pre-fill the form fields.
        """
        db_file = database_path_locator()
        conn = sqlite3.connect(db_file)

        try:
            cursor = conn.cursor()
            # Query to fetch employee data
            cursor.execute('''
                SELECT FName, LName, Email, ContactNo, Role 
                FROM EMPLOYEE 
                WHERE EmployeeID = ?
            ''', (selected_employee_id,))
            employee_data = cursor.fetchone()

            if employee_data:
                fname, lname, email, contact_no, role = employee_data

                # Pre-fill the form fields
                fname_entry.insert(0, fname)
                lname_entry.insert(0, lname)
                email_entry.insert(0, email)
                contact_no_entry.insert(0, contact_no)
                role_combobox.set(role)
            else:
                messagebox.showerror("Error", "Employee not found.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Could not fetch employee data: {e}")
        finally:
            conn.close()


    def submit_form():
        """
        Handle form submission.
        Collects data from the form fields and processes it (e.g., save to a database).
        """
        fname = fname_entry.get()
        lname = lname_entry.get()
        email = email_entry.get()
        contact_no = contact_no_entry.get()
        role = role_combobox.get()
        createdby = user_id

        # Validate inputs (optional but recommended)
        if not fname or not lname or not email or not contact_no or not role:
            print("All fields are required!")
            return
        db_file = database_path_locator()
        conn = sqlite3.connect(db_file)

        try:
            # Perform database operation
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE EMPLOYEE
                SET FName = ?, 
                    LName = ?, 
                    Email = ?, 
                    ContactNo = ?, 
                    Role = ?, 
                    CreatedBy = ?
                WHERE EmployeeID = ?
            ''', (fname, lname, email, contact_no, role, createdby, selected_employee_id))
            conn.commit()
            print("Employee edited successfully!")
            # Clear the form after successful submission
            clear_form()
            show_employee_table(table)
            root.destroy()
        except sqlite3.IntegrityError as e:
            # Handle unique constraint violation or other integrity errors
            messagebox.showerror("Error", f"Could not edit employee: {e}")
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
        contact_no_entry.delete(0, tk.END)
        role_combobox.set('')

    root = tk.Tk()
    root.title("Edit Employee Form")
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

    tk.Label(root, text="Contact No:", font=("Helvetica", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
    contact_no_entry = tk.Entry(root, font=("Helvetica", 12))
    contact_no_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(root, text="Role:", font=("Helvetica", 12)).grid(row=5, column=0, padx=10, pady=5, sticky="w")
    role_combobox = ttk.Combobox(root, values=["Cataloger", "Librarian", "Admin", "Staff"], font=("Helvetica", 12),
                                 state="readonly")
    role_combobox.grid(row=5, column=1, padx=10, pady=5)

    # Call populate_form to pre-fill the form
    populate_form()

    # Buttons for Submit and Cancel
    button_frame = tk.Frame(root)
    button_frame.grid(row=6, column=0, columnspan=2, pady=20)

    submit_button = tk.Button(button_frame, text="Submit", font=("Helvetica", 12), command=submit_form)
    submit_button.grid(row=0, column=0, padx=10)

    cancel_button = tk.Button(button_frame, text="Cancel", font=("Helvetica", 12), command=cancel_form)
    cancel_button.grid(row=0, column=1, padx=10)