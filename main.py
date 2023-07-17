import csv
import tkinter as tk
from tkinter import messagebox, simpledialog
from csv import DictWriter
import pandas as pd
from pandastable import Table, TableModel

# Main Window
window = tk.Tk()
window.title("Boat Food Inventory Manager")

def add_entry():
    name = simpledialog.askstring("Product Name", "Enter the product name")
    quantity = simpledialog.askstring("Quantity", "Enter the quantity")
    expiry_date = simpledialog.askstring("Expiry Date", "Enter the expiry date (YYYY-MM-DD)")
    tags = simpledialog.askstring("Tags", "Enter the tags")
    
    with open('boat_food.csv', 'a+', newline='') as write_obj:
        dictwriter_object = DictWriter(write_obj, fieldnames=['Product Name', 'Quantity', 'Expiry Date', 'Tags'])
        dictwriter_object.writerow({'Product Name': name, 'Quantity': quantity, 'Expiry Date': expiry_date, 'Tags': tags})
        write_obj.close()
    load_table()

def load_table():
    try:
        data_frame = pd.read_csv('boat_food.csv')
        table = pt = Table(table_frame, dataframe=data_frame, showtoolbar=True, showstatusbar=True)
        pt.show()
    except FileNotFoundError:
        pass

def delete_entry():
    del_product = simpledialog.askstring("Product Name", "Enter the name of the product to delete")
    lines = list()
    with open('boat_food.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == del_product:
                    lines.remove(row)
    with open('boat_food.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    load_table()

# Button to add entries
add_button = tk.Button(window, text="Add Entry", command=add_entry)
add_button.pack()

# Button to delete entries
delete_button = tk.Button(window, text="Delete Entry", command=delete_entry)
delete_button.pack()

# Table Frame
table_frame = tk.Frame(window)
table_frame.pack(fill='both', expand=True)

load_table()

window.mainloop()
