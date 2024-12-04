import tkinter as tk
from Log_In.log_in import log_in_page
from Admin.Admin import admin_page



def start_app():
    """
    Entry point for the application.
    Starts with the login page.
    """
    root = tk.Tk()
    root.title("Main Application")
    log_in_page(root, switch_to_admin)

def switch_to_admin(root, user_id):
    """
    Switches to the admin page.
    :param root: Current Tkinter root window
    :param user_id: Logged-in user ID
    """
    # Destroy the current window
    root.destroy()
    # Start the admin page
    admin_page(user_id, switch_to_login)

def switch_to_login():
    """
    Switches back to the login page.
    """
    # Create a new root window for login
    root = tk.Tk()
    root.title("Login")
    log_in_page(root, switch_to_admin)