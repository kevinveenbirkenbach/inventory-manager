from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox
import pandas as pd

class View(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QtWidgets.QTableWidget()
        self.layout.addWidget(self.table)

        self.add_button = QtWidgets.QPushButton('Add Entry')
        self.layout.addWidget(self.add_button)

        self.delete_button = QtWidgets.QPushButton('Delete Entry')
        self.layout.addWidget(self.delete_button)

        self.save_button = QtWidgets.QPushButton('Save Changes')
        self.layout.addWidget(self.save_button)

        self.reload_button = QtWidgets.QPushButton('Reload Inventory')
        self.layout.addWidget(self.reload_button)

    def show_table(self, data_frame):
        self.table.setRowCount(0)
        self.table.setColumnCount(len(data_frame.columns))
        self.table.setHorizontalHeaderLabels(data_frame.columns)
        for i, row in data_frame.iterrows():
            self.table.insertRow(i)
            for j, cell in enumerate(row):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(cell)))
