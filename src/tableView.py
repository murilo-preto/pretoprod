from functions.parser import parse_work_logs

import tkinter as tk
from tkinter import ttk

# Function to parse work log files and extract structured data


# Function to display the logs using a Tkinter GUI
def display_logs(logs):
    root = tk.Tk()
    root.title("Work Log Viewer")
    
    # Create a frame to hold the widgets
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    # Create a Treeview widget to display the log entries
    tree = ttk.Treeview(frame, columns=("Time", "Activity"), show="headings")
    tree.heading("Time", text="Time")
    tree.heading("Activity", text="Activity")
    tree.grid(row=1, column=0, columnspan=2)
    
    # Function to load and display the log entries for the selected date
    def load_log(index):
        # Clear the existing entries in the Treeview
        for row in tree.get_children():
            tree.delete(row)
        log = logs[index]
        # Insert the new entries into the Treeview
        for entry in log["entries"]:
            tree.insert("", tk.END, values=(entry["time"], entry["activity"]))
    
    # Create a dropdown menu to select the date of the log to display
    log_dates = [log["date"] for log in logs]
    selected_log = tk.StringVar()
    dropdown = ttk.Combobox(frame, textvariable=selected_log, values=log_dates)
    dropdown.grid(row=0, column=0)
    # Bind the selection event to the load_log function
    dropdown.bind("<<ComboboxSelected>>", lambda e: load_log(log_dates.index(selected_log.get())))
    
    root.mainloop()

# Example usage:
logs = parse_work_logs("makeshift_data")
if logs:
    display_logs(logs)
