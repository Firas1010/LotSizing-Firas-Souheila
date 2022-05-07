from PyQt5 import QtCore, QtGui, QtWidgets
from QEC_Interface import Ui_QEC_Interface
from LFL_Interface import Ui_LFL_Interface
from SM_Interface import Ui_SilverMeal_Interface
from EOP_Interface import Ui_EOP_Interface
from PPB_Interface import Ui_PPB_Interface
from ME_Interface import Ui_ME_Interface
from LUC_Interface import Ui_LUC_Interface


class Ui_JCH(object):
    def OpenQEC(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_QEC_Interface()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenLFL(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_LFL_Interface()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenEOP(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_EOP_Interface()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenLUC(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_LUC_Interface()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenPPB(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_PPB_Interface()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenSM(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_SilverMeal_Interface()
                self.ui.setupUi(self.window)
                self.window.show()
    def OpenME(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_ME_Interface()
                self.ui.setupUi(self.window)
                self.window.show()
    def setupUi(self, JCH):
        JCH.setObjectName("JCH")
        JCH.resize(402, 432)
        self.widget = QtWidgets.QWidget(JCH)
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


        self.retranslateUi(JCH)
        QtCore.QMetaObject.connectSlotsByName(JCH)

    def retranslateUi(self, JCH):
        _translate = QtCore.QCoreApplication.translate
        JCH.setWindowTitle(_translate("JCH", "Choix Heuristique"))
        
        self.LFLbtn.setText(_translate("JCH", "Lot For Lot"))

        self.QECbtn.setText(_translate("JCH", "Economic Order Quantity"))

        self.POQbtn.setText(_translate("JCH", "Period Order Quantity"))

        self.LUCbtn.setText(_translate("JCH", "Least Unit Cost"))
        
        self.PPB.setText(_translate("JCH", "Part Period Balancing "))
        
        self.SMbtn.setText(_translate("JCH", "Silver-Meal"))

        self.MEbtn.setText(_translate("JCH", "Méthodes exactes"))
        self.label.setText(_translate("JCH", "Choisir une méthode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JCH = QtWidgets.QWidget()
    ui = Ui_JCH()
    ui.setupUi(JCH)
    JCH.show()
    sys.exit(app.exec_())
