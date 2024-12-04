import sqlite3
from tkinter import ttk, messagebox
from DATABASEFUNCTION.Database_path_function import database_path_locator

def show_employee_table(table: ttk.Treeview):
    """
    Fetch and display employee data in the given Treeview table.
    :param table: The ttk.Treeview widget where the employee data will be displayed.
    """
    # Database path setup (modify if needed)
    db_file = database_path_locator()

    # Clear existing rows in the table
    for item in table.get_children():
        table.delete(item)

    try:
        # Connect to the database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Fetch employee data
        query = "SELECT EmployeeID, FName || ' ' || LName AS Name, Role, ContactNo, CreatedBy FROM Employee WHERE Softdelete = 0"
        cursor.execute(query)
        employees = cursor.fetchall()

        # Populate the table
        for emp in employees:
            table.insert("", "end", values=emp)

        print("Employee data displayed successfully.")
    except sqlite3.Error as e:
        print(f"Error fetching employee data: {e}")
    finally:
        conn.close()

