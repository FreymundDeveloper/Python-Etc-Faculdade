import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Janela(QWidget):
    __listWidget = None
    __lineEdit = None
    __add_bt = None
    __clear_bt = None
    __delete_bt = None

    def __init__(self, Str="Janela", x1=0, y1=0, dx=640, dy=480, cor="lightgray"):
        super().__init__()
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)

        self.inicialize()

    def add_item(self):
        if self.__lineEdit.text() == '':
            self.__lineEdit.setText('')
        else:
            self.__listWidget.addItem(self.__lineEdit.text())

    def clear_item(self):
        self.__listWidget.clear()

    def delete_item(self):
        self.__listWidget.takeItem(self.__listWidget.currentRow())

    def closeEvent(self, event):
        self.destroy()
        sys.exit(0)

    def inicialize(self):
        self.__listWidget = QListWidget(self)
        self.__listWidget.setGeometry(100, 100, 300, 300)

        self.__add_bt = QPushButton(self)
        self.__add_bt.setText('ADD')
        self.__add_bt.move(10, 10)

        self.__clear_bt = QPushButton(self)
        self.__clear_bt.setText('CLEAR')
        self.__clear_bt.move(190, 10)

        self.__delete_bt = QPushButton(self)
        self.__delete_bt.setText('DELETE')
        self.__delete_bt.move(350, 10)

        self.__lineEdit = QLineEdit(self)
        self.__lineEdit.setGeometry(145, 70, 200, 20)

        self.__add_bt.clicked.connect(self.add_item)
        self.__clear_bt.clicked.connect(self.clear_item)
        self.__delete_bt.clicked.connect(self.delete_item)

        self.show()


App = QApplication(sys.argv)
Jan1 = Janela("Lista Widget", 0, 0, 500, 500, "lightgray")
App.exec_()
