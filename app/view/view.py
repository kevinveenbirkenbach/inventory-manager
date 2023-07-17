from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem

class View(QtWidgets.QWidget):
    deleteSignal = QtCore.pyqtSignal(int)
    editSignal = QtCore.pyqtSignal(QTableWidgetItem) 
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QtWidgets.QTableWidget()
        self.layout.addWidget(self.table)

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['UUID', 'Product Name', 'Quantity', 'Expiry Date', 'Location', 'Tags', 'Delete'])
        self.table.itemChanged.connect(self.edit_entry)

    def show_table(self, data_frame):
        self.table.setRowCount(0)
        for row_index, row_data in data_frame.iterrows():
            self.table.insertRow(row_index)
            for column_index, cell_data in enumerate(row_data):
                if isinstance(cell_data, list):
                    cell_text = ', '.join(cell_data)
                else:
                    cell_text = str(cell_data)
                item = QtWidgets.QTableWidgetItem(cell_text)
                self.table.setItem(row_index, column_index, item)
            delete_button = QtWidgets.QPushButton('Delete')
            delete_button.clicked.connect(lambda row=row_index: self.delete_entry(row))
            self.table.setCellWidget(row_index, 6, delete_button)

        # Always add an empty row at the end
        self.table.insertRow(self.table.rowCount())

    def get_text_input(self, title, message):
        text, ok = QtWidgets.QInputDialog.getText(self, title, message)
        return text, ok

    def show_message(self, title, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.exec_()

    def delete_entry(self, row):
        self.deleteSignal.emit(row)  # Emit the signal

    def edit_entry(self, item):
        self.editSignal.emit(item) 