# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiGrafo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(673, 430)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/grafo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.txtImage = QtWidgets.QTextEdit(Form)
        self.txtImage.setGeometry(QtCore.QRect(0, 0, 671, 431))
        self.txtImage.setAccessibleDescription("")
        self.txtImage.setAutoFillBackground(False)
        self.txtImage.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtImage.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.txtImage.setTabChangesFocus(False)
        self.txtImage.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txtImage.setObjectName("txtImage")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Grafo"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
