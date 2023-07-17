import tkinter as tk
from pandastable import Table, TableModel

class View:
    def __init__(self, window):
        self.window = window
        self.table_frame = tk.Frame(window)
        self.table_frame.pack(fill='both', expand=True)
        self.add_button = tk.Button(window, text="Add Entry")
        self.add_button.pack()
        self.delete_button = tk.Button(window, text="Delete Entry")
        self.delete_button.pack()
        self.save_button = tk.Button(window, text="Save Changes")
        self.save_button.pack()
        self.reload_button = tk.Button(window, text="Reload Inventory")
        self.reload_button.pack()

    def show_table(self, data_frame):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        table_model = TableModel(data_frame)
        table = Table(self.table_frame, dataframe=data_frame, model=table_model, showtoolbar=True, showstatusbar=True)
        table.show()
        self.window.update_idletasks()  # Add this line
        self.window.geometry('')  # Reset the geometry

