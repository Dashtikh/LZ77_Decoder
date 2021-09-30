from PyQt5 import QtCore, QtGui, QtWidgets
from lz77 import *
from lz78 import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelEnter = QtWidgets.QLabel(self.centralwidget)
        self.labelEnter.setGeometry(QtCore.QRect(40, 30, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelEnter.setFont(font)
        self.labelEnter.setObjectName("labelEnter")
        self.inputData = QtWidgets.QTextEdit(self.centralwidget)
        self.inputData.setGeometry(QtCore.QRect(40, 80, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputData.setFont(font)
        self.inputData.setObjectName("inputData")
        self.radioLz77 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioLz77.setGeometry(QtCore.QRect(40, 150, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioLz77.setFont(font)
        self.radioLz77.setObjectName("radioLz77")
        self.radioLz78 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioLz78.setGeometry(QtCore.QRect(120, 150, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioLz78.setFont(font)
        self.radioLz78.setObjectName("radioLz78")
        self.encodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.encodeButton.setGeometry(QtCore.QRect(260, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.encodeButton.setFont(font)
        self.encodeButton.setObjectName("encodeButton")
        self.encodeResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.encodeResultLabel.setGeometry(QtCore.QRect(50, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.encodeResultLabel.setFont(font)
        self.encodeResultLabel.setObjectName("encodeResultLabel")
        self.decodeResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.decodeResultLabel.setGeometry(QtCore.QRect(50, 340, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.decodeResultLabel.setFont(font)
        self.decodeResultLabel.setObjectName("decodeResultLabel")
        self.encodedData = QtWidgets.QLabel(self.centralwidget)
        self.encodedData.setGeometry(QtCore.QRect(180, 240, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.encodedData.setFont(font)
        self.encodedData.setObjectName("encodedData")
        self.decodedData = QtWidgets.QLabel(self.centralwidget)
        self.decodedData.setGeometry(QtCore.QRect(180, 340, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.decodedData.setFont(font)
        self.decodedData.setObjectName("decodedData")
        self.decodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.decodeButton.setGeometry(QtCore.QRect(400, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decodeButton.setFont(font)
        self.decodeButton.setObjectName("decodeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # when Encode Button clicked
        self.encodeButton.clicked.connect(lambda: self.encodeClicked(self.inputData.toPlainText()))

        # when Decode Button clicked
        self.decodeButton.clicked.connect(lambda: self.decodeClicked(self.inputData.toPlainText()))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LZ77 - LZ78"))
        self.labelEnter.setText(_translate("MainWindow", "Enter encoded or decoded data"))
        self.radioLz77.setText(_translate("MainWindow", "lz77"))
        self.radioLz77.setChecked(True)
        self.radioLz78.setText(_translate("MainWindow", "lz78"))
        self.encodeButton.setText(_translate("MainWindow", "Encode"))
        self.encodeResultLabel.setText(_translate("MainWindow", "Encoded data"))
        self.decodeResultLabel.setText(_translate("MainWindow", "Decoded data"))
        self.encodedData.setText(_translate("MainWindow", ""))
        self.decodedData.setText(_translate("MainWindow", ""))
        self.decodeButton.setText(_translate("MainWindow", "Decode"))

    def encodeClicked(self, data):
        if self.radioLz77.isChecked():
            self.encodedData.setText(encoder77(data))
        else:
            print("Lz78 encoder")

    def decodeClicked(self, data):
        if self.radioLz77.isChecked():
            self.decodedData.setText(decoder77(data))
        else:
            self.decodedData.setText(decoder78(data))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
