from PyQt5 import QtCore, QtGui, QtWidgets
from HebdoChoix_Heurstique import Ui_HCH
from Choix_Heurstique import Ui_JCH
from AnnuelChoix_Heurstique import Ui_ACH


class Ui_Cnx(object):
    def Openjour(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_JCH()
                self.ui.setupUi(self.window)

                self.window.show()
    def Openannuel(self):

                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_ACH()
                self.ui.setupUi(self.window)

                self.window.show()
    def Openhebdo(self):
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_HCH()
                self.ui.setupUi(self.window)

                self.window.show()
    def setupUi(self, Cnx):
        Cnx.setObjectName("Cnx")
        Cnx.resize(803, 302)
        self.widget = QtWidgets.QWidget(Cnx)
        self.widget.setGeometry(QtCore.QRect(0, 0, 811, 301))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(150, 120, 221, 51))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"border-radius:20px;\n"
"font: 75 18pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 120, 221, 51))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"border-radius:20px;\n"
"font: 75 18pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 210, 251, 51))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"border-radius:20px;\n"
"font: 75 18pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(200, 40, 461, 41))
        self.label.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 28pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(0, 170, 221, 131))
        self.widget_2.setStyleSheet("border-image: url(:/pic/logo.PNG);")
        self.widget_2.setObjectName("widget_2")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(580, 170, 221, 131))
        self.widget_5.setStyleSheet("border-image: url(:/pic/logo.PNG);")
        self.widget_5.setObjectName("widget_5")
        self.pushButton_3.raise_()
        self.label.raise_()
        self.widget_2.raise_()
        self.pushButton.raise_()
        self.widget_5.raise_()
        self.pushButton_2.raise_()
        self.pushButton.clicked.connect(self.Openjour)
        self.pushButton_2.clicked.connect(self.Openannuel)
        self.pushButton_3.clicked.connect(self.Openhebdo)
        self.retranslateUi(Cnx)
        QtCore.QMetaObject.connectSlotsByName(Cnx)

    def retranslateUi(self, Cnx):
        _translate = QtCore.QCoreApplication.translate
        Cnx.setWindowTitle(_translate("Cnx", "Choix de période"))
        self.pushButton.setText(_translate("Cnx", "Lot Sizing journalière"))
        self.pushButton_2.setText(_translate("Cnx", "Lot Sizing Annuelle"))
        self.pushButton_3.setText(_translate("Cnx", "Lot Sizing Hebomadaire"))
        self.label.setText(_translate("Cnx", "Choisir la période de travail"))
import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cnx = QtWidgets.QWidget()
    ui = Ui_Cnx()
    ui.setupUi(Cnx)
    Cnx.show()
    sys.exit(app.exec_())
