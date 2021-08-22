from PyQt5 import QtCore, QtGui, QtWidgets
import antiv
import os


class Ui_MainWindow(object):
    d = ["C:\\"]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.joel_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.joel_tableWidget.setGeometry(QtCore.QRect(0, 60, 611, 441))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.joel_tableWidget.setFont(font)
        self.joel_tableWidget.setObjectName("joel_tableWidget")
        self.joel_tableWidget.setColumnCount(2)
        self.joel_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.joel_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.joel_tableWidget.setHorizontalHeaderItem(1, item)
        self.ref_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ref_pushButton.setGeometry(QtCore.QRect(20, 520, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ref_pushButton.setFont(font)
        self.ref_pushButton.setObjectName("ref_pushButton")
        self.rem_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rem_pushButton.setGeometry(QtCore.QRect(240, 520, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.rem_pushButton.setFont(font)
        self.rem_pushButton.setObjectName("rem_pushButton")
        self.upd_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.upd_pushButton.setGeometry(QtCore.QRect(430, 520, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.upd_pushButton.setFont(font)
        self.upd_pushButton.setObjectName("upd_pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 441, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.joel_tableWidget.selectionModel(
        ).selectionChanged.connect(self.on_selectionChanged)

    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row+1)
        col = 0
        for item in row_data:
            cell = QtWidgets.QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

    def _removeRow(self, table):
        while table.rowCount() > 0:
            table.removeRow(table.rowCount()-1)

    def insert_data(self):
        self.label.setText("Scanning")
        self._removeRow(self.joel_tableWidget)
        self.list1 = antiv.search(self.d)
        for each in self.list1:
            self.addTableRow(self.joel_tableWidget, each)
        if self.list1 == []:
            self.label.setText("There is no virus")
        else:
            self.label.setText("There a total "+str(len(self.list1))+" files")

    def on_selectionChanged(self, selected, deselected):
        for ix in selected.indexes():
            print("Selected cell location row : {0}, column: {1}".format(
                ix.row(), ix.column()))
            self.rem = self.list1[int(ix.row())][1]

    def remove_data(self):
        os.remove(self.rem)
        self.label.setText("File Removed")

    def update_data(self):
        antiv.update()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.joel_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "File"))
        item = self.joel_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Path"))
        self.ref_pushButton.setText(_translate("MainWindow", "Refresh"))
        self.rem_pushButton.setText(_translate("MainWindow", "Remove"))
        self.upd_pushButton.setText(_translate("MainWindow", "Update"))
        self.label.setText(_translate("MainWindow", ""))
        self.ref_pushButton.clicked.connect(self.insert_data)
        self.rem_pushButton.clicked.connect(self.remove_data)
        self.upd_pushButton.clicked.connect(self.update_data)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
