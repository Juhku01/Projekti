import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__ (self):
        QMainWindow.__init__(self)
        self.resize(500,500)

        self.container = QFrame()
        self.container.setObjectName("Container")
        self.container.setStyleSheet("#container {background-color:#222 }")
        self.layout = QVBoxLayOut()

        self.toggle = QPushButton("Test")
        self.layout.addWidget(self.toggle, Qt.AlingCenter, Qt.AlingCenter)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
