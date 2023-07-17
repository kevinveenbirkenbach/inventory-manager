import tkinter as tk
from tkinter import messagebox, simpledialog
from app.model.model import Model
from app.view.view import View

class Controller:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Boat Food Inventory Manager")
        self.model = Model()
        self.view = View(self.window)
        self.view.add_button['command'] = self.add_entry
        self.view.delete_button['command'] = self.delete_entry
        self.view.save_button['command'] = self.save_changes
        self.view.reload_button['command'] = self.load_data
        self.load_data()

    def add_entry(self):
        name = simpledialog.askstring("Product Name", "Enter the product name")
        quantity = simpledialog.askstring("Quantity", "Enter the quantity")
        expiry_date = simpledialog.askstring("Expiry Date", "Enter the expiry date (YYYY-MM-DD)")
        tags = simpledialog.askstring("Tags", "Enter the tags separated by comma without spaces")
        self.model.add_entry(name, quantity, expiry_date, tags)
        self.model.save_changes()
        self.load_data()

    def delete_entry(self):
        del_product = simpledialog.askstring("Product Name", "Enter the name of the product to delete")
        self.model.delete_entry(del_product)
        self.model.save_changes()
        self.load_data()

    def save_changes(self):
        self.model.save_changes()
        self.load_data()
        messagebox.showinfo("Save Success", "The changes have been successfully saved.")

    def load_data(self):
        try:
            self.model.load_data()
            self.view.show_table(self.model.data_frame)
        except FileNotFoundError:
            pass

    def run(self):
        self.window.mainloop()
