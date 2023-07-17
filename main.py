import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
from pandastable import Table, TableModel
import json

# Main Window
window = tk.Tk()
window.title("Boat Food Inventory Manager")

data_frame = pd.DataFrame(columns=['Product Name', 'Quantity', 'Expiry Date', 'Tags'])

def add_entry():
    global data_frame
    name = simpledialog.askstring("Product Name", "Enter the product name")
    quantity = simpledialog.askstring("Quantity", "Enter the quantity")
    expiry_date = simpledialog.askstring("Expiry Date", "Enter the expiry date (YYYY-MM-DD)")
    tags = simpledialog.askstring("Tags", "Enter the tags separated by comma without spaces")

    data_frame.loc[len(data_frame)] = [name, quantity, expiry_date, tags]
    save_changes()
    load_table()

def load_table():
    global data_frame
    for widget in table_frame.winfo_children():
        widget.destroy()

    try:
        with open('boat_food.json') as json_file:
            data = json.load(json_file)
        data_frame = pd.DataFrame(data)
        table_model = TableModel(data_frame)
        table = Table(table_frame, dataframe=data_frame, model=table_model, showtoolbar=True, showstatusbar=True)
        table.show()
    except FileNotFoundError:
        pass

def save_changes():
    global data_frame
    data = data_frame.to_dict(orient='records')
    with open('boat_food.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    messagebox.showinfo("Save Success", "The changes have been successfully saved.")

def delete_entry():
    global data_frame
    del_product = simpledialog.askstring("Product Name", "Enter the name of the product to delete")
    data_frame = data_frame[data_frame['Product Name'] != del_product]
    save_changes()
    load_table()

# Button to add entries
add_button = tk.Button(window, text="Add Entry", command=add_entry)
add_button.pack()

# Button to delete entries
delete_button = tk.Button(window, text="Delete Entry", command=delete_entry)
delete_button.pack()

# Button to save changes
save_button = tk.Button(window, text="Save Changes", command=save_changes)
save_button.pack()

# Table Frame
table_frame = tk.Frame(window)
table_frame.pack(fill='both', expand=True)

load_table()

window.mainloop()
