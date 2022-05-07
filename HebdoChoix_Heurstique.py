from PyQt5 import QtCore, QtGui, QtWidgets
from QEC_InterfaceHebdo import Ui_QECHebdo
from LFL_InterfaceHebdo import Ui_LFLHebdo
from SM_InterfaceHebdo import Ui_SMHebdo
from EPQ_InterfaceHebdo import Ui_EPQHebdo
from PPB_InterfaceHebdo import Ui_PPBHebdo
from ME_InterfaceHebdo import Ui_MEHebdo
from LUC_InterfaceHebdo import Ui_LUCHebdo

class Ui_HCH(object):
    def OpenQEC(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_QECHebdo()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenLFL(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_LFLHebdo()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenEOP(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_EPQHebdo()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenLUC(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_LUCHebdo()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenPPB(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_PPBHebdo()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenSM(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_SMHebdo()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenME(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_MEHebdo()
                self.ui.setupUi(self.window)
                self.window.show()

    def setupUi(self, HCH):
        HCH.setObjectName("HCH")
        HCH.resize(402, 432)
        self.widget = QtWidgets.QWidget(HCH)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 431))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.LFLbtn = QtWidgets.QPushButton(self.widget)
        self.LFLbtn.setGeometry(QtCore.QRect(10, 70, 381, 41))
        self.LFLbtn.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 127), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.LFLbtn.setObjectName("LFLbtn")
        self.QECbtn = QtWidgets.QPushButton(self.widget)
        self.QECbtn.setGeometry(QtCore.QRect(10, 120, 381, 41))
        self.QECbtn.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 127), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.QECbtn.setObjectName("QECbtn")
        self.POQbtn = QtWidgets.QPushButton(self.widget)
        self.POQbtn.setGeometry(QtCore.QRect(10, 170, 381, 41))
        self.POQbtn.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 127), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.POQbtn.setObjectName("POQbtn")
        self.LUCbtn = QtWidgets.QPushButton(self.widget)
        self.LUCbtn.setGeometry(QtCore.QRect(10, 220, 381, 41))
        self.LUCbtn.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 127), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.LUCbtn.setObjectName("LUCbtn")
        self.PPB = QtWidgets.QPushButton(self.widget)
        self.PPB.setGeometry(QtCore.QRect(10, 270, 381, 41))
        self.PPB.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 127), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.PPB.setObjectName("PPB")
        self.SMbtn = QtWidgets.QPushButton(self.widget)
        self.SMbtn.setGeometry(QtCore.QRect(10, 320, 381, 41))
        self.SMbtn.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 127), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.SMbtn.setObjectName("SMbtn")
        self.MEbtn = QtWidgets.QPushButton(self.widget)
        self.MEbtn.setGeometry(QtCore.QRect(10, 370, 381, 41))
        self.MEbtn.setStyleSheet("border-radius:20px;\n"
"font: 75 22pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(0, 0, 127), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);")
        self.MEbtn.setObjectName("MEbtn")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(60, 20, 291, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 28pt \"Playball\";")
        self.label.setObjectName("label")
        self.QECbtn.clicked.connect(self.OpenQEC)
        self.LFLbtn.clicked.connect(self.OpenLFL)
        self.POQbtn.clicked.connect(self.OpenEOP)
        self.LUCbtn.clicked.connect(self.OpenLUC)
        self.PPB.clicked.connect(self.OpenPPB)
        self.SMbtn.clicked.connect(self.OpenSM)
        self.MEbtn.clicked.connect(self.OpenSM)
        self.retranslateUi(HCH)
        QtCore.QMetaObject.connectSlotsByName(HCH)

    def retranslateUi(self, HCH):
        _translate = QtCore.QCoreApplication.translate
        HCH.setWindowTitle(_translate("HCH", "Choix Heuristique"))

        self.LFLbtn.setText(_translate("HCH", "Lot For Lot"))

        self.QECbtn.setText(_translate("HCH", "Economic Order Quantity"))

        self.POQbtn.setText(_translate("HCH", "Period Order Quantity"))

        self.LUCbtn.setText(_translate("HCH", "Least Unit Cost"))
 
        self.PPB.setText(_translate("HCH", "Part Period Balancing "))

        self.SMbtn.setText(_translate("HCH", "Silver-Meal"))

        self.MEbtn.setText(_translate("HCH", "Méthodes exactes"))
        self.label.setText(_translate("HCH", "Choisir une méthode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HCH = QtWidgets.QWidget()
    ui = Ui_HCH()
    ui.setupUi(HCH)
    HCH.show()
    sys.exit(app.exec_())
