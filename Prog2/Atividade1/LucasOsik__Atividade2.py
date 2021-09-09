import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Janela(QWidget):
    __combo = None
    __label = None
    __label2 = None
    __button = None

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

    def go(self):
        self.__label2.setText(str(self.__combo.currentIndex()))

    def closeEvent(self, event):
        self.destroy()
        sys.exit(0)

    def inicialize(self):
        self.__combo = QComboBox(self)
        self.__combo.move(50, 5)
        self.__combo.addItem('text')
        self.__combo.addItem('text1')
        self.__combo.addItem('text2')
        self.__combo.addItem('text3')
        self.__combo.addItem('text4')
        self.__combo.addItem('text5')

        self.__combo.setStyleSheet('color:red')

        self.__label2 = QLabel(self)
        self.__label2.move(140, 100)

        self.__label = QLabel(self)
        self.__label.setText("The index is " + self.__label2.text())
        self.__label.move(50, 100)

        self.__button = QPushButton(self)
        self.__button.setText('go')
        self.__button.move(50, 50)
        self.__button.clicked.connect(self.go)

        self.show()


App = QApplication(sys.argv)
App.setStyle('windows')
Jan1 = Janela("Janela", 0, 0, 250, 150, "lightgray")
App.exec_()
