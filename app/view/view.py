from PyQt5 import QtWidgets, QtGui

class View(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QtWidgets.QTableWidget()
        self.layout.addWidget(self.table)

        self.add_button = QtWidgets.QPushButton('Add Entry')
        self.layout.addWidget(self.add_button)

        self.save_button = QtWidgets.QPushButton('Save Changes')
        self.layout.addWidget(self.save_button)

        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Product Name', 'Quantity', 'Expiry Date', 'Tags', 'Delete'])

    def show_table(self, data_frame):
        self.table.setRowCount(0)
        for i, row in data_frame.iterrows():
            self.table.insertRow(i)
            for j, cell in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(cell))
                self.table.setItem(i, j, item)
            delete_button = QtWidgets.QPushButton('Delete')
            delete_button.clicked.connect(lambda row=i: self.delete_entry(row))
            self.table.setCellWidget(i, 4, delete_button)

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
        self.controller.delete_entry(row)

