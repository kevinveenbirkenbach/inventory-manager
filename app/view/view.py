from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem

class View(QtWidgets.QWidget):
    deleteSignal = QtCore.pyqtSignal(int)
    editSignal = QtCore.pyqtSignal(QTableWidgetItem) 

    # Add signals for increment and decrement actions
    incrementSignal = QtCore.pyqtSignal(int)
    decrementSignal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QtWidgets.QTableWidget()
        self.layout.addWidget(self.table)

        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['UUID', 'Product Name', 'Quantity', 'Expiry Date', 'Location', 'Tags', 'Inc', 'Dec', 'Delete'])
        self.table.itemChanged.connect(self.edit_entry)
        self.table.setItemDelegateForColumn(2, IntegerDelegate(self))

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

            increment_button = QtWidgets.QPushButton('+')
            increment_button.clicked.connect(lambda checked, x=row_index: self.increment(x))
            self.table.setCellWidget(row_index, 6, increment_button)

            decrement_button = QtWidgets.QPushButton('-')
            decrement_button.clicked.connect(lambda checked, x=row_index: self.decrement(x))
            self.table.setCellWidget(row_index, 7, decrement_button)

            delete_button = QtWidgets.QPushButton('Delete')
            delete_button.clicked.connect(lambda row=row_index: self.delete_entry(row))
            self.table.setCellWidget(row_index, 8, delete_button)

        # Always add an empty row at the end
        self.table.insertRow(self.table.rowCount())

    # Add increment and decrement functions
    def increment(self, row):
        self.incrementSignal.emit(row)

    def decrement(self, row):
        self.decrementSignal.emit(row)

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

from PyQt5 import QtWidgets, QtCore, QtGui
class IntegerDelegate(QtWidgets.QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QLineEdit(parent)
        reg_ex = QtCore.QRegExp("[0-9]+.?[0-9]{,2}")
        input_validator = QtGui.QRegExpValidator(reg_ex, editor)
        editor.setValidator(input_validator)
        return editor