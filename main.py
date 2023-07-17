import csv
import tkinter as tk
from tkinter import messagebox, simpledialog
from csv import DictWriter
import pandas as pd
from pandastable import Table, TableModel

# Main Window
window = tk.Tk()
window.title("Boat Food Inventory Manager")

data_frame = pd.DataFrame(columns=['Product Name', 'Quantity', 'Expiry Date', 'Tags'])
table_model = TableModel(data_frame)

def add_entry():
    name = simpledialog.askstring("Product Name", "Enter the product name")
    quantity = simpledialog.askstring("Quantity", "Enter the quantity")
    expiry_date = simpledialog.askstring("Expiry Date", "Enter the expiry date (YYYY-MM-DD)")
    tags = simpledialog.askstring("Tags", "Enter the tags")
    
    with open('boat_food.csv', 'a+', newline='') as write_obj:
        dictwriter_object = DictWriter(write_obj, fieldnames=['Product Name', 'Quantity', 'Expiry Date', 'Tags'])
        if write_obj.tell() == 0:
            dictwriter_object.writeheader()
        dictwriter_object.writerow({'Product Name': name, 'Quantity': quantity, 'Expiry Date': expiry_date, 'Tags': tags})
    load_table()

def load_table():
    global data_frame
    global table_model
    for widget in table_frame.winfo_children():
        widget.destroy()

    try:
        data_frame = pd.read_csv('boat_food.csv')
        table_model = TableModel(data_frame)
        table = Table(table_frame, dataframe=data_frame, model=table_model, showtoolbar=True, showstatusbar=True)
        table.show()
    except FileNotFoundError:
        pass

def save_changes():
    global data_frame
    data_frame.to_csv('boat_food.csv', index=False)
    messagebox.showinfo("Save Success", "The changes have been successfully saved.")

def delete_entry():
    del_product = simpledialog.askstring("Product Name", "Enter the name of the product to delete")
    global data_frame
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
