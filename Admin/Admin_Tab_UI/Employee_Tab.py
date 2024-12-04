import tkinter as tk
from tkinter import ttk, messagebox
from Admin.Admin_functions.Accounts_fetch import show_employee_table
from Admin.Admin_forms.Admin_Create_Employee_Form import creation_emp_form
from Admin.Admin_forms.Admin_Edit_Employee_Form import edit_emp_form
from Admin.Admin_functions.Account_Soft_Delete import delete_employee
selected_employee_id = None



def employee_tab(user_id, table_section, footer):
    def add_handler():
        creation_emp_form(user_id, table)

    def on_row_select(event):
        global selected_employee_id
        selected_item = table.selection()

        if not selected_item:
            return None

        item_data = table.item(selected_item[0])['values']
        if not item_data:
            selected_employee_id = None
            messagebox.showerror("Error", "Selected row has no data!")
            return

        selected_employee_id = item_data[0]  # EmployeeID
        print(f"Selected Employee ID: {selected_employee_id}")

    def edit_handle():
        if not selected_employee_id:
            messagebox.showerror("Error", "No employee selected for editing.")
            return

        edit_emp_form(user_id, table, selected_employee_id)

    def delete_handle():
        # Show confirmation prompt
        confirm = messagebox.askyesno("Confirm Deletion",
                                      f"Are you sure you want to delete employee ID {selected_employee_id}?")
        if confirm:  # If user clicks 'Yes', proceed with deletion
            delete_employee(selected_employee_id, table)
        else:  # If user clicks 'No', cancel the operation
            messagebox.showinfo("Cancelled", "Employee deletion cancelled.")

    # Create a table using Treeview
    columns = ("ID", "Name", "Role", "Contact", "Created by")
    table = ttk.Treeview(table_section, columns=columns, show="headings", height=15)
    scrollbar = ttk.Scrollbar(table_section, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Define column headings
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=150, anchor="center")

    # Populate table with data
    show_employee_table(table)
    table.bind('<<TreeviewSelect>>', on_row_select)

    # Pack the table
    table.pack(fill="both", expand=True, padx=10, pady=10)

    # Footer Buttons for CRUD
    footer.grid_columnconfigure((0, 1, 2), weight=1)

    tk.Button(footer, text="Add", width=10, command=add_handler).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    tk.Button(footer, text="Edit", width=10, command=edit_handle).grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    tk.Button(footer, text="Delete", width=10, command=delete_handle).grid(row=0, column=2, padx=10, pady=10, sticky="e")