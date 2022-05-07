import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QHBoxLayout,QMessageBox,QPushButton,QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Interface_Cnx import  Ui_Cnx
import os

class Ui_APP(object):
    def message(self):
            msg=QMessageBox()
            msg.setWindowTitle("APropos")
            msg.setText("Application pour résoudre le probléme de lot sizing.\n"
"Développée par Firas Houimel et Souheila Bouaïcha\n"
"comme étant un projet de fin d\'année 2021-2022.\n"
"Cette application contient 3 façon pour calculer la ME\n"
"(Wagner & Whitin) et 6 méthodes approchées\n"
"(LFL, EOQ, LUC, Silver Meal, PPB, POQ)."
"Une Méthode pour calculer la solution optimale \n"
"Selon une planification Journalière,hebdomadaire et Annuelle \n")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
    def warinig(self):
            msg=QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("Saisir Votre mot de passe")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
    def OpenFirstInterface(self):
            PW=self.PW.text()
            if PW=='GSIL' :
                self.window = QtWidgets.QMainWindow()
                self.ui= Ui_Cnx()
                self.ui.setupUi(self.window)
                APP.hide()
                self.window.show()
            else :
                msg=QMessageBox()
                msg.setWindowTitle("Erreur")
                msg.setText("Saisir Votre mot de passe")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_() 


    def facebook(self):
        F = QApplication(sys.argv) 
        web = QWebEngineView()
        web.load(QUrl("https://www.facebook.com/houimel.firas/"))
        web.show()
        sys.exit(F.exec_())  
    def twitter(self):
        APP = QApplication(sys.argv) 
        web = QWebEngineView()
        web.load(QUrl("https://twitter.com/houimel_firas"))
        web.show()  
        APP.exec_()
    def LinkedIn(self):
        app = QApplication(sys.argv) 
        web = QWebEngineView()
        web.load(QUrl("https://www.linkedin.com/in/souheila-bouaicha-1748911b4/?originalSubdomain=tn"))
        web.show()  
    def Mail(self):
        app = QApplication(sys.argv) 
        web = QWebEngineView()
        web.load(QUrl("https://mail.google.com/mail/u/0/#inbox"))
        web.show()   
    def setupUi(self, APP):
        APP.setObjectName("APP")
        APP.resize(662, 412)
        APP.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        APP.setAttribute(QtCore.Qt.WA_TranslucentBackground)  
        self.widget_2 = QtWidgets.QWidget(APP)
        self.widget_2.setGeometry(QtCore.QRect(0, 160, 661, 251))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 50px;")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(90, 50, 161, 41))
        self.label.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 26pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.OK = QtWidgets.QPushButton(self.widget_2)
        self.OK.setGeometry(QtCore.QRect(450, 50, 91, 41))
        self.OK.setStyleSheet("QPushButton#OK{\n"
"border-radius:20px;\n"
"font: 75 26pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"color:rgba(255, 255, 255, 210);"
"}\n"
"QPushButton#OK:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#OK:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.OK.setObjectName("OK")
        self.PW = QtWidgets.QLineEdit(self.widget_2)
        self.PW.setGeometry(QtCore.QRect(240, 50, 171, 41))
        self.PW.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 26pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW.setObjectName("PW")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 571, 111))
        self.label_2.setStyleSheet("border-image: url(:/pic/logo.PNG);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.mail = QtWidgets.QPushButton(self.widget_2)
        self.mail.setGeometry(QtCore.QRect(380, 220, 31, 21))
        self.mail.setStyleSheet("QPushButton#mail{\n"
"border-image: url(:/pic/Mail-icon.png);"
"}\n"
"QPushButton#mail:hover{\n"

"}\n"
"QPushButton#mail:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"}")
        self.mail.setText("")
        self.mail.setObjectName("mail")
        self.Twitter_2 = QtWidgets.QPushButton(self.widget_2)
        self.Twitter_2.setGeometry(QtCore.QRect(330, 220, 31, 21))
        self.Twitter_2.setStyleSheet("QPushButton#Twitter_2{\n"
"border-image: url(:/pic/linkedin-icon.png);"
"}\n"
"QPushButton#Twitter_2:hover{\n"

"}\n"
"QPushButton#Twitter_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"}")
        self.Twitter_2.setText("")
        self.Twitter_2.setObjectName("Twitter_2")
        self.Twitter = QtWidgets.QPushButton(self.widget_2)
        self.Twitter.setGeometry(QtCore.QRect(280, 220, 31, 21))
        self.Twitter.setStyleSheet("QPushButton#Twitter{\n"
"border-image: url(:/pic/twitter-icon.png);"
"}\n"
"QPushButton#Twitter:hover{\n"

"}\n"
"QPushButton#Twitter:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"}")
        self.Twitter.setText("")
        self.Twitter.setObjectName("Twitter")
        self.FB = QtWidgets.QPushButton(self.widget_2)
        self.FB.setGeometry(QtCore.QRect(230, 220, 31, 21))
        self.FB.setStyleSheet("QPushButton#FB{\n"
"border-image: url(:/pic/social-facebook-button-blue-icon.png);"
"}\n"
"QPushButton#FB:hover{\n"

"}\n"
"QPushButton#FB:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"}")
        self.FB.setText("")
        self.FB.setObjectName("FB")
        self.INFo = QtWidgets.QPushButton(APP)
        self.INFo.setGeometry(QtCore.QRect(610, 20, 31, 21))
        self.INFo.setStyleSheet("border-image: url(:/pic/Button-Info-icon.png);")
        self.INFo.setText("")
        self.INFo.setObjectName("INFo")
        self.EXIT = QtWidgets.QPushButton(APP)
        self.EXIT.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.EXIT.setStyleSheet("border-image: url(:/pic/Alarm-Error-icon.png);")
        self.EXIT.setText("")
        self.EXIT.setObjectName("EXIT")
        self.widget = QtWidgets.QWidget(APP)
        self.widget.setGeometry(QtCore.QRect(0, 0, 661, 201))
        self.widget.setStyleSheet("border-image: url(:/pic/visuel-site-problemes-industrie-1200x700.jpg);\n"
"border-top-left-radius: 50px;\n"
"border-top-right-radius: 50px;")
        self.widget.setObjectName("widget")
        self.widget_2.raise_()
        self.widget.raise_()
        self.EXIT.raise_()
        self.INFo.raise_()
        self.OK.clicked.connect(self.OpenFirstInterface)
        self.EXIT.clicked.connect(APP.close)       
        self.INFo.clicked.connect(self.message)

        # self.FB.clicked.connect(self.facebook)
        # self.Twitter.clicked.connect(self.twitter)
        # self.Twitter_2.clicked.connect(self.LinkedIn)
        # self.mail.clicked.connect(self.Mail)
        self.retranslateUi(APP)
        QtCore.QMetaObject.connectSlotsByName(APP)

    def retranslateUi(self, APP):
        _translate = QtCore.QCoreApplication.translate
        APP.setWindowTitle(_translate("APP", "APP"))
        self.label.setText(_translate("APP", "Password"))
        self.PW.setPlaceholderText(_translate("APP", "*******"))

        self.OK.setText(_translate("APP", "OK"))
import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    APP = QtWidgets.QWidget()
    ui = Ui_APP()
    ui.setupUi(APP)
    APP.show()
    sys.exit(app.exec_())
