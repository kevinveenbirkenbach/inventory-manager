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
        self.load_data()
        self.view.deleteSignal.connect(self.delete_entry)  # Connect the signal
        self.view.editSignal.connect(self.edit_entry)  # Connect the signal

    def edit_entry(self, item):
        row = item.row()
        uuid_item = self.view.table.item(row, 0)
        if row == self.view.table.rowCount() - 1:
            self.add_entry(row);
        else:
            self.update_entry(item)    
        self.model.save_changes()
        self.load_data()

    def update_entry(self, item):
        row = item.row()
        uuid_item = self.view.table.item(row, 0)
        uuid = uuid_item.text()
        column = item.column()
        value = item.text()
        self.model.data_frame.loc[self.model.data_frame['uuid'] == uuid, self.model.data_frame.columns[column]] = value
    
    def add_entry(self,row):
        values = [self.view.table.item(row, col).text() if self.view.table.item(row, col) else '' for col in range(self.view.table.columnCount())]
        self.model.add_entry(*values[-5:])

    def delete_entry(self, row):
        uuid = self.view.table.item(row, 0).text()  # Fetch the UUID from the table
        self.model.delete_entry(uuid)
        self.model.save_changes()
        self.load_data()

    def load_data(self):
        self.view.table.blockSignals(True)
        try:
            self.model.load_data()
            self.view.show_table(self.model.data_frame)
        except FileNotFoundError:
            pass
        self.view.table.blockSignals(False) 

    def run(self):
        self.window.show()
        self.app.exec_()
