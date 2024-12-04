import sqlite3
from tkinter import messagebox
from DATABASEFUNCTION.Database_path_function import database_path_locator
from Admin.Admin_functions.Accounts_fetch import show_employee_table


def delete_employee(employee_id, table):
    """
    Marks the employee with the given employee_id as deleted in the EMPLOYEE table.
    """
    if not employee_id:
        messagebox.showerror("Error", "No employee selected for deletion.")
        return

    # Confirm deletion with the user

    db_file = database_path_locator()
    conn = sqlite3.connect(db_file)

    try:
        cursor = conn.cursor()
        # Perform the soft delete by setting softdelete = 1
        cursor.execute('''
            UPDATE EMPLOYEE
            SET softdelete = ?
            WHERE EmployeeID = ?
        ''', (1, employee_id))
        conn.commit()

        # Confirm deletion
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", f"Employee ID {employee_id} marked as deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Employee not found or already deleted.")

        # Refresh the table view
        table.delete(*table.get_children())  # Clear current table
        show_employee_table(table)  # Reload updated table data
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Failed to delete employee: {e}")
    finally:
        conn.close()