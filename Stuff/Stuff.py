import tkinter as tk
from tkinter import ttk
from datetime import datetime

def staff_ui():
    def time_in():
        """
        Handle the Time In button click.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Time In recorded at {current_time}")
        tk.messagebox.showinfo("Time In", f"Time In recorded at {current_time}")

    def time_out():
        """
        Handle the Time Out button click.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Time Out recorded at {current_time}")
        tk.messagebox.showinfo("Time Out", f"Time Out recorded at {current_time}")

    # Create the main window
    root = tk.Tk()
    root.title("Staff Schedule")
    root.geometry("600x400")  # Adjust as needed

    # Schedule Table
    table_frame = tk.Frame(root)
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    columns = ("Schedule ID", "Day", "Start Time", "End Time", "Description")
    table = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

    # Add a vertical scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Define column headings
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, anchor="center")  # Adjust column width

    table.pack(fill="both", expand=True)

    # Footer Buttons
    footer = tk.Frame(root)
    footer.pack(fill="x", padx=10, pady=10)

    time_in_button = tk.Button(footer, text="Time In", font=("Helvetica", 12), command=time_in, width=10)
    time_in_button.pack(side="left", padx=10)

    time_out_button = tk.Button(footer, text="Time Out", font=("Helvetica", 12), command=time_out, width=10)
    time_out_button.pack(side="right", padx=10)

    root.mainloop()

# Call the function to display the UI
staff_ui()