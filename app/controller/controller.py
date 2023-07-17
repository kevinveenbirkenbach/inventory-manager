from PyQt5 import QtWidgets
from app.model.model import Model
from app.view.view import View

class Controller:
    def __init__(self, data_dir=None):
        self.app = QtWidgets.QApplication([])
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("Inventory Manager")

        self.model = Model(data_dir)
        self.view = View(self.window)
        self.view.controller = self  
        self.window.setCentralWidget(self.view)
        self.load_data()
        self.view.deleteSignal.connect(self.delete_entry)
        self.view.editSignal.connect(self.edit_entry)

        # Connect new signals
        self.view.incrementSignal.connect(self.increment_entry)
        self.view.decrementSignal.connect(self.decrement_entry)

    def increment_entry(self, row):
        uuid = self.view.table.item(row, 0).text()  
        quantity = self.model.data_frame.loc[self.model.data_frame['uuid'] == uuid, 'quantity']
        self.model.data_frame.loc[self.model.data_frame['uuid'] == uuid, 'quantity'] = quantity.astype(int) + 1
        self.model.save_changes()
        self.load_data()

    def decrement_entry(self, row):
        uuid = self.view.table.item(row, 0).text()  
        quantity = self.model.data_frame.loc[self.model.data_frame['uuid'] == uuid, 'quantity'].astype(int)
        if quantity.iloc[0] > 0:
            self.model.data_frame.loc[self.model.data_frame['uuid'] == uuid, 'quantity'] = quantity - 1
            self.model.save_changes()
            self.load_data()


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
    
    def add_entry(self, row):
        values = [self.view.table.item(row, col).text() if self.view.table.item(row, col) else '' for col in range(self.view.table.columnCount())]
        self.model.add_entry(*values[1:6])


    def delete_entry(self, row):
        uuid = self.view.table.item(row, 0).text()  # Fetch the UUID from the table
        self.model.delete_entry(uuid)
        self.model.save_changes()
        self.load_data()

    def load_data(self):
        self.view.table.blockSignals(True)
        try:
            self.model.load_data()
            #self.model.data_frame['quantity'] = self.model.data_frame['quantity'].astype(int)
            self.view.show_table(self.model.data_frame)
        except FileNotFoundError:
            pass
        self.view.table.blockSignals(False) 

    def run(self):
        self.window.show()
        self.app.exec_()
