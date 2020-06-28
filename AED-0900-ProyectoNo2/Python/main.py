import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from Nucleo.mainWindow import mainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = mainWindow()
    main.show()
    sys.exit(app.exec_())
