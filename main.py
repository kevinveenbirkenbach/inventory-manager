import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
from pandastable import Table, TableModel
import json


class Model:
    def __init__(self):
        self.data_frame = pd.DataFrame(columns=['Product Name', 'Quantity', 'Expiry Date', 'Tags'])

    def add_entry(self, name, quantity, expiry_date, tags):
        self.data_frame.loc[len(self.data_frame)] = [name, quantity, expiry_date, tags]

    def delete_entry(self, del_product):
        self.data_frame = self.data_frame[self.data_frame['Product Name'] != del_product]

    def save_changes(self):
        data = self.data_frame.to_dict(orient='records')
        with open('boat_food.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def load_data(self):
        with open('boat_food.json', 'r') as json_file:
            data = json.load(json_file)
        self.data_frame = pd.DataFrame(data)


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

    def show_table(self, data_frame):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        table_model = TableModel(data_frame)
        table = Table(self.table_frame, dataframe=data_frame, model=table_model, showtoolbar=True, showstatusbar=True)
        table.show()


class Controller:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Boat Food Inventory Manager")
        self.model = Model()
        self.view = View(self.window)
        self.view.add_button['command'] = self.add_entry
        self.view.delete_button['command'] = self.delete_entry
        self.view.save_button['command'] = self.save_changes
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
        messagebox.showinfo("Save Success", "The changes have been successfully saved.")

    def load_data(self):
        try:
            self.model.load_data()
            self.view.show_table(self.model.data_frame)
        except FileNotFoundError:
            pass

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Controller()
    app.run()
