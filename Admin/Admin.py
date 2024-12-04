import tkinter as tk
from Admin.Admin_functions.Account_credential_fetch import user_credentials
from Admin.Admin_Tab_UI.Employee_Tab import employee_tab


def admin_page(user_id, switch_to_login):
    def tab_handler(tab_name):
        """
        Handle tab switching based on the button clicked.
        Clears the right-side frame and loads the selected tab's content.
        """
        # Clear current content in table_section
        for widget in table_section.winfo_children():
            widget.destroy()
        for widget in footer.winfo_children():
            widget.destroy()

        if tab_name == "EMPLOYEE":
            employee_tab(user_id, table_section, footer)
        elif tab_name == "TAB 2":
            tk.Label(table_section, text="Tab 2 Content").pack(pady=20)
        elif tab_name == "TAB 3":
            tk.Label(table_section, text="Tab 3 Content").pack(pady=20)

    def logout_handler():
        """
        Handle the logout process.
        """
        root.destroy()  # Close the current window
        switch_to_login()  # Navigate back to the login page

    # Fetch user credentials (e.g., first and last name)
    first_name, last_name = user_credentials(user_id)

    # Main window setup
    root = tk.Tk()
    root.title("Admin Page")
    root.geometry("1000x700")

    # Configure grid for dynamic resizing
    root.grid_rowconfigure(1, weight=1)  # Row for main content expands
    root.grid_columnconfigure(1, weight=1)  # Right-side area expands

    # Left Sidebar
    sidebar = tk.Frame(root, bg="lightgray", width=150)
    sidebar.grid(row=0, column=0, rowspan=3, sticky="ns")  # Fill vertically

    # Sidebar Buttons
    tk.Button(sidebar, text="EMPLOYEE", height=2, width=15,
              command=lambda: tab_handler("EMPLOYEE")).pack(pady=10)
    tk.Button(sidebar, text="TAB 2", height=2, width=15,
              command=lambda: tab_handler("TAB 2")).pack(pady=10)
    tk.Button(sidebar, text="TAB 3", height=2, width=15,
              command=lambda: tab_handler("TAB 3")).pack(pady=10)

    # Name Display Section (Bottom of Sidebar)
    name_display = tk.Frame(sidebar, bg="lightgray")
    name_display.pack(side="bottom", pady=20)

    tk.Label(name_display, text=f"{first_name}", font=("Helvetica", 12), bg="lightgray").pack(pady=2)
    tk.Label(name_display, text=f"{last_name}", font=("Helvetica", 12), bg="lightgray").pack(pady=2)

    # Logout Button
    logout_button = tk.Button(name_display, text="Logout", font=("Helvetica", 10), bg="red", fg="white",
                               command=logout_handler)
    logout_button.pack(pady=10)  # Add some padding below the last name

    # Header Section
    header = tk.Frame(root, bg="lightblue", height=50)
    header.grid(row=0, column=1, sticky="ew")  # Fill horizontally
    header.grid_columnconfigure(0, weight=1)

    tk.Label(header, text="Admin Dashboard", bg="lightblue", font=("Helvetica", 16)).pack(pady=10)

    # Main Table Section
    table_section = tk.Frame(root, bg="white")
    table_section.grid(row=1, column=1, sticky="nsew")  # Expandable section



    # Footer Section (Now strictly on the right side)
    footer = tk.Frame(root, bg="lightgray", height=50)
    footer.grid(row=2, column=1, sticky="ew")  # Only spans the right column

    root.mainloop()
