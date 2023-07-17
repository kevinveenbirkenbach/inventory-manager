from PyQt5 import QtWidgets

from app.model.model import Model
from app.view.view import View

class Controller:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("Boat Food Inventory Manager")

        self.model = Model()
        self.view = View(self.window)
        self.view.controller = self  # Set the reference to the controller in the view
        self.window.setCentralWidget(self.view)

        self.view.add_button.clicked.connect(self.add_entry)
        self.view.save_button.clicked.connect(self.save_changes)

        self.load_data()

    def add_entry(self):
        name, ok = self.view.get_text_input('Product Name', 'Enter the product name:')
        quantity, ok = self.view.get_text_input('Quantity', 'Enter the quantity:')
        expiry_date, ok = self.view.get_text_input('Expiry Date', 'Enter the expiry date (YYYY-MM-DD):')
        location, ok = self.view.get_text_input('Location', 'Enter the location:')
        tags, ok = self.view.get_text_input('Tags', 'Enter the tags separated by comma without spaces:')
        if ok:
            self.model.add_entry(name, quantity, expiry_date, location, tags)
            self.model.save_changes()
            self.load_data()

    def delete_entry(self, row):
        self.model.delete_entry(row)
        self.model.save_changes()
        self.load_data()

    def save_changes(self):
        self.model.save_changes()
        self.load_data()
        self.view.show_message('Save Success', 'The changes have been successfully saved.')

    def load_data(self):
        try:
            self.model.load_data()
            self.view.show_table(self.model.data_frame)
        except FileNotFoundError:
            pass

    def run(self):
        self.window.show()
        self.app.exec_()
